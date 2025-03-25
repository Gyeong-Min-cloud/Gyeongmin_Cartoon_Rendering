import cv2
import numpy as np

def cartoonize_image(img):
    # 1. 이미지 블러 처리 (스무딩)
    img_color = cv2.bilateralFilter(img, 9, 75, 75)  # 양방향 필터 강도를 낮춰서 선명하게

    # 2. 그레이스케일로 변환 후 엣지 강조 (윤곽선)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 3)  # 미디언 블러 강도 줄임

    # 3. 엣지 디텍션 (선명하게 엣지 강조)
    img_edge = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, 11, 9)  # 엣지 선명도를 더 높임

    # 4. 컬러 이미지와 엣지를 합성
    img_cartoon = cv2.bitwise_and(img_color, img_color, mask=img_edge)

    return img_cartoon

# 이미지 로드 (image.png로 파일 경로 변경)
img = cv2.imread('image.png')  # 이미지 파일 경로를 'image.png'로 설정

# 카툰화 처리
cartoon_img = cartoonize_image(img)

# 결과 이미지 보여주기
cv2.imshow('Cartoonized Image', cartoon_img)

# 키를 눌러서 창 종료
cv2.waitKey(0)
cv2.destroyAllWindows()
