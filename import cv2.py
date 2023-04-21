import cv2

# 웹캠 열기
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 정상적으로 읽어졌다면
    if ret:
        # 좌우반전
        flipped_frame = cv2.flip(frame, 1)

        # 흑백으로 변환
        gray_frame = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)

        # 변환된 프레임 보여주기
        cv2.imshow('flipped gray frame', gray_frame)

    # q를 누르면 종료
    if cv2.waitKey(1) == ord('q'):
        break

# 모든 윈도우 닫기
cv2.destroyAllWindows()

# 웹캠 해제
cap.release()
