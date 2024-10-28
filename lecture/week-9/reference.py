import cv2
import numpy as np

def DrawCircle(image, y, x):
    """
    Fungsi untuk menggambar lingkaran pada gambar pada koordinat tertentu.
    """
    center_coor = (x, y)  # Koordinat pusat lingkaran (x, y)
    radius = 2  # Jari-jari lingkaran
    color = (255, 0, 0)  # Warna lingkaran (Biru dalam format BGR)
    thickness = 2  # Ketebalan garis lingkaran

    # Menggambar lingkaran pada gambar
    image = cv2.circle(image, center_coor, radius, color, thickness)
    return image

# Akses kamera
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error opening camera")
    exit()

while True:
    # Ambil frame dari kamera
    ret, frame = cam.read()
    if not ret:
        print("Error in retrieving frame")
        break

    # Konversi frame ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Batas bawah dan atas warna hijau dalam HSV
    lower = np.array([40, 40, 40])
    upper = np.array([80, 255, 255])

    # Buat mask untuk deteksi warna hijau
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.bitwise_not(mask)  # Membalik mask

    # Kernel untuk operasi morfologi
    kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.uint8)

    # Salin mask
    m = mask.copy()

    # Operasi erosi dan dilasi untuk mengurangi noise
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Ambil hanya bagian foreground dari frame
    foreground = cv2.bitwise_and(frame, frame, mask=mask)

    # Komponen yang terhubung dalam mask
    num_labels, labels_im = cv2.connectedComponents(mask)

    # Loop melalui setiap komponen terhubung (kecuali background)
    for i in range(1, num_labels):
        b, k = np.where(labels_im == i)

        # Mendapatkan batas-batas dari komponen terhubung
        bmin = b.min()
        xbmin = k[np.where(b == bmin)[0][0]]

        bmax = b.max()
        xbmax = k[np.where(b == bmax)[0][0]]

        kmin = k.min()
        kmax = k.max()
        ykmin = b[np.where(k == kmin)[0][0]]
        ykmax = b[np.where(k == kmax)[0][0]]

        # Menampilkan informasi komponen
        print(i)
        print("Baris:", bmin, bmax)
        print("Kolom:", kmin, kmax)

        # Gambar lingkaran di sekitar batas-batas komponen
        frame = DrawCircle(frame, bmin, xbmin)
        frame = DrawCircle(frame, bmax, xbmax)
        frame = DrawCircle(frame, ykmin, kmin)
        frame = DrawCircle(frame, ykmax, kmax)

    # Tampilkan hasil
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('m', m)
    cv2.imshow('fr', foreground)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) == ord('q'):
        break

# Lepaskan resource kamera dan tutup semua jendela
cam.release()
cv2.destroyAllWindows()
