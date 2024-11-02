#第一次執行時要安裝的東西

#產生虛擬環境
python -m venv venv
source venv/bin/activate

# 1. 安装构建工具
pip install build twine

# 2.可以來上傳了 
./sh/pypi.sh