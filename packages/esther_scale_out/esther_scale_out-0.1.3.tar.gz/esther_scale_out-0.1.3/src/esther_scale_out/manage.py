import os
import time
import psutil
import requests
import subprocess

# 필요한 환경 변수
LINE_NOTIFY_TOKEN = os.getenv("ACCESS_TOKEN")

# Docker Compose 파일 경로 (필요에 맞게 수정)
COMPOSE_FILE = "docker-compose.yml"

# LINE Notify 메시지 전송 함수
def send_line_notification(message):
    headers = {
        "Authorization": f"Bearer {LINE_NOTIFY_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"message": message}
    response = requests.post(
        "https://notify-api.line.me/api/notify",
        headers=headers,
        data=data
    )
    if response.status_code == 200:
        print("LINE 알림 전송 완료:", message)
    else:
        print("LINE 알림 전송 실패:", response.text)

# Docker Compose 서비스 시작
def start_docker_compose():
    print("Docker Compose 서비스를 시작합니다...")
    subprocess.run(["docker", "compose", "-f", COMPOSE_FILE, "up", "-d"], check=True)

# 현재 Docker Compose 서비스의 인스턴스 수 확인
def get_current_scale(service_name="blog"):
    result = subprocess.run(
        ["docker", "compose", "ps", "-q", service_name],
        capture_output=True, text=True
    )
    containers = result.stdout.splitlines()
    return len(containers)

# 스케일 아웃 (Docker Compose 서비스 인스턴스 증가)
def scale_out(service_name="blog"):
    current_scale = get_current_scale(service_name)
    new_scale = current_scale + 1
    print(f"스케일 아웃: {service_name} 인스턴스를 {new_scale}개로 설정합니다.")
    subprocess.run(["docker", "compose", "up", "--scale", f"{service_name}={new_scale}", "-d"], check=True)
    send_line_notification(f"{service_name} 서비스가 스케일 아웃되어 {new_scale}개 인스턴스로 확장되었습니다.")

# 스케일 인 (Docker Compose 서비스 인스턴스 감소)
def scale_in(service_name="blog"):
    current_scale = get_current_scale(service_name)
    if current_scale > 1:
        new_scale = current_scale - 1
        print(f"스케일 인: {service_name} 인스턴스를 {new_scale}개로 설정합니다.")
        subprocess.run(["docker", "compose", "up", "--scale", f"{service_name}={new_scale}", "-d"], check=True)
        send_line_notification(f"{service_name} 서비스가 스케일 인되어 {new_scale}개 인스턴스로 축소되었습니다.")

# CPU 사용량 체크 함수
def get_cpu_utilization():
    return psutil.cpu_percent(interval=1)  # 1초간 CPU 사용량 측정

# CPU 사용량을 모니터링하고 스케일 인/아웃을 수행하는 함수
def monitor_and_scale(threshold=50, check_interval=10):
    over_threshold_time = 0

    while True:
        cpu_utilization = get_cpu_utilization()
        print(f"현재 CPU 사용량: {cpu_utilization:.2f}%")

        # CPU 사용량이 임계치를 초과한 시간이 1분 이상일 때 스케일 아웃
        if cpu_utilization > threshold:
            over_threshold_time += check_interval
            if over_threshold_time >= 30:
                scale_out()
                over_threshold_time = 0  # 스케일 아웃 후 시간 초기화
        # CPU 사용량이 기준의 절반 이하로 떨어지면 스케일 인
        else:
            if over_threshold_time > 0:
                over_threshold_time -= check_interval
            elif cpu_utilization < threshold / 2:
                scale_in()

        time.sleep(check_interval)  # CPU 사용량 체크 주기

def main():
    if not LINE_NOTIFY_TOKEN:
        print("LINE Notify 토큰이 설정되지 않았습니다. 환경 변수를 확인해주세요.")
    else:
        print("Docker Compose 서비스를 시작하고 CPU 모니터링을 시작합니다...")
        start_docker_compose()
        monitor_and_scale()
