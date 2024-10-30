# auto_scailer
config.ini에 설정된 값에 따라 container의 수를 자동적으로 증감하는 프로그램으로, 원할한 시스템 운영에 기여합니다. 

### Usage
```bash
$ scailer-start
```

### Dependency
- requests

### Versions
- `1.0.1` : 실행중인 container가 없는 경우에 대한 처리 (프로그램 종료)
- `1.0.0` : 정식 배포, LINE NOTIFY 추가
- `0.5.0` : 데모

### Reference
- [configparser](https://docs.python.org/3/library/configparser.html)
- [패키징 가이드](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages)
