# main.py
import importlib.metadata
import subprocess
import sys
import requests
from packaging import version

def install_package_if_missing(package_name):
    try:
        # Kiểm tra xem package đã được cài chưa
        importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        # Nếu chưa cài đặt thì tiến hành cài đặt
        # print(f"{package_name} chưa được cài đặt. Đang tiến hành cài đặt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def check_for_updates():
    try:
        # Lấy phiên bản hiện tại của mrjpacking
        current_version = importlib.metadata.version("mrjpacking")
        
        # Lấy thông tin phiên bản mới nhất từ PyPI
        response = requests.get("https://pypi.org/pypi/mrjpacking/json", timeout=5)
        if response.status_code == 200:
            latest_version = response.json()["info"]["version"]
            
            # So sánh phiên bản
            if version.parse(latest_version) > version.parse(current_version):
                print(f"Đã có phiên bản mới {latest_version}.")
                choice = input("Bạn có muốn cập nhật không? (y/n): ").strip().lower()
                if choice == "y":
                    update_package()
                else:
                    run_mrjpacking()
            else:
                print(f"Phiên bản hiện tại {current_version} là phiên bản mới nhất.")
                run_mrjpacking()
        else:
            print("Không thể kiểm tra phiên bản mới.")
            run_mrjpacking()
    except Exception as e:
        print("Lỗi cập nhật:", e)
        run_mrjpacking()

def update_package():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "mrjpacking"])
        print("Đã cập nhật phiên bản thành công!")
        run_mrjpacking()
    except Exception as e:
        print("Có lỗi khi cập nhật:", e)
        run_mrjpacking()

def run_mrjpacking():
    try:
        import mrjpacking
        mrjpacking.run()  # Gọi hàm chạy chính của mrjpacking
    except ImportError:
        # print("Không tìm thấy gói 'mrjpacking'. Hãy cài đặt trước khi tiếp tục.")\
        install_package_if_missing("mrjpacking")
        import mrjpacking
        mrjpacking.run()

if __name__ == "__main__":
    # Kiểm tra và cài đặt mrjpacking nếu chưa có
    install_package_if_missing("mrjpacking")
    # Sau đó kiểm tra phiên bản và cập nhật nếu cần
    check_for_updates()
