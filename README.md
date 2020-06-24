# HostMonitor
monitor metadata of influxdb and ES, rest api support for CRUD metadata and results

![framework](./HostMonitor.png)

# 安装

    python3 -m pip install -r requirements.txt

# 运行

    # 请用 python3.6 以上版本运行
    python3 main.py --env=local
    # browser open http://localhost:8000/

# TO DO
- [x] framework
- [x] http rest api
- [ ] json body parser
- [ ] async ES backend
- [ ] async influxdb backend
- [ ] query factory / abstract method
- [ ] operator
- [ ] unittest
- [ ] directory document
- [ ] docker file
