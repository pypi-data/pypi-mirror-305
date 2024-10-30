from auto_scailer.utils import get_limit, get_cpu_use, send_line_noti
import time
import os

conti_high=0
conti_low=0

def auto_scailer():
    global conti_high
    global conti_low

    scale_in_value, scale_out_value=map(float,get_limit())

    home_path=os.path.expanduser("~")
    cu, scale_cnt =get_cpu_use()
    while scale_cnt:
        print(f"[INFO] 현재 CPU사용량은 {cu}입니다.")
        print(f"[INFO] 현재 container의 수는 {scale_cnt}개입니다.")
        #### CPU 사용량이 scale_out_value를 넘으면 scale out ####
        if float(cu.replace("%",""))>scale_out_value:
            conti_high+=10
            print(f"[WARN] {conti_high}초 동안 과부하 상태...")
        else:
            conti_high=0

        if conti_high==60:
            print(f"[INFO] container의 수를 {scale_cnt+1}로 scale out 합니다.")
            os.system(f"docker compose -f {home_path}/code/docker/k1s/docker-compose.yaml up -d --scale blog={scale_cnt+1}")

            conti_high=0
            code, msg = send_line_noti(f"[INFO] container의 수가 {scale_cnt+1}로 scale out 되었습니다.")


        ######################################################
        #### CPU 사용량이 scale_in_value보다 낮으면 scale in ####
        ##### 1개의 컨테이너는 남겨야 함 ########################
        if scale_cnt>1:
            if float(cu.replace("%",""))<scale_in_value:
                conti_low+=10
                print(f"[INFO] {conti_low}초 동안 안정된 상태...")
            else:
                conti_low=0

            if conti_low==60:
                    print(f"[INFO] container의 수를 {scale_cnt-1}로 scale in 합니다.", end="\n\n")
                    os.system(f"docker compose -f {home_path}/code/docker/k1s/docker-compose.yaml up -d --scale blog={scale_cnt-1}")

                    conti_low=0
                    code, msg = send_line_noti(f"[INFO] container의 수가 {scale_cnt-1}로 scale in 되었습니다.")
        ######################################################
        print("")
        time.sleep(10)
        cu, scale_cnt =get_cpu_use()