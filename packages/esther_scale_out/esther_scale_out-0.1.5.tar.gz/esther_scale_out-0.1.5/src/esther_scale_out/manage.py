import os
import time
import psutil
import requests
import subprocess

LINE_NOTIFY_TOKEN = os.getenv("ACCESS_TOKEN")
COMPOSE_FILE = "docker-compose.yml"

def send_line_notification(message):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
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

def start_docker_compose():
    print("Docker Compose 서비스를 시작합니다...")
    subprocess.run(["docker compose", "-f", COMPOSE_FILE, "up", "-d"], check=True)

def scale_out(service_name="blog", target_scale=2):
    print(f"스케일 아웃: {service_name} 인스턴스를 {target_scale}개로 설정합니다.")
    subprocess.run(["docker compose", "-f", COMPOSE_FILE, "up", "--scale", f"{service_name}={target_scale}", "-d"], check=True)
    send_line_notification(f"{service_name} 서비스가 스케일 아웃되어 {target_scale}개 인스턴스로 확장되었습니다.")

def scale_in(service_name="blog", target_scale=1):
    print(f"스케일 인: {service_name} 인스턴스를 {target_scale}개로 설정합니다.")
    subprocess.run(["docker compose", "-f", COMPOSE_FILE, "up", "--scale", f"{service_name}={target_scale}", "-d"], check=True)
    send_line_notification(f"{service_name} 서비스가 스케일 인되어 {target_scale}개 인스턴스로 축소되었습니다.")

def get_cpu_utilization():
    return psutil.cpu_percent(interval=1)

def monitor_and_scale(threshold=30, check_interval=10):
    over_threshold_time = 0
    while True:
        cpu_utilization = get_cpu_utilization()
        print(f"현재 CPU 사용량: {cpu_utilization:.2f}%")
        if cpu_utilization > threshold:
            over_threshold_time += check_interval
            if over_threshold_time >= 20:  # 20초 지속 시 스케일 아웃
                scale_out()
                over_threshold_time = 0
        else:
            if over_threshold_time > 0:
                over_threshold_time -= check_interval
            elif cpu_utilization < threshold / 2:
                scale_in()
        time.sleep(check_interval)

# main 함수 정의
def main():
    if not LINE_NOTIFY_TOKEN:
        print("LINE Notify 토큰이 설정되지 않았습니다. 환경 변수를 확인해주세요.")
    else:
        print("Docker Compose 서비스를 시작하고 CPU 모니터링을 시작합니다...")
        start_docker_compose()
        monitor_and_scale()
