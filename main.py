import yt_dlp

urls = [
    "https://youtu.be/1f18irP--O8?si=Xa1iEHqi0aqF5lLA",
    "https://youtu.be/lgvtusNiHQo?si=fcsq7HtP4cZXJ7Cv",
    "https://youtu.be/C5COEOYyAow?si=q3wi1EBajsLGcDlu",
    "https://youtu.be/TTkjAOt2i70?si=DiT1tlz4o5qRcyH_",
    "https://youtu.be/gEmahl1XMB0?si=-hKBVM5uqxYzY2yj",
    "https://youtu.be/99NUJ1cLbBI?si=ftv55IIjlSRqg0I1",
    "https://youtu.be/JW5ZlV-ZkRA?si=qSeTJkEKNUDF0pIx",
    "https://youtu.be/J2JQQm1h6xQ?si=Zt7dfsJ_8OIdIUJ6",
    "https://youtu.be/Tt-mCnzPK-o?si=KRoiXsQmk_z6x5PC",
    "https://youtu.be/XTJKSjqmCpk?si=5K6Ai9WvvsQU7sb-",
    "https://youtu.be/2Vv-BfVoq4g?si=mEfHB7WOE-L5M4yN",
    "https://youtu.be/kffacxfA7G4?si=9HJHUkSiViGqK2AJ",
    "https://youtu.be/3AtDnEC4zak?si=u1lLb9tiM5wKhsxm",
    "https://youtu.be/0KSOMA3QBU0?si=RjcVSc64ifHtjprN",
    "https://youtu.be/kPa7bsKwL-c?si=-1HVraI-6u1uReKw",
    "https://youtu.be/uPD0QOGTmMI?si=mNM9w6LfQV2sw0HK",
    "https://youtu.be/ic8j13piAhQ?si=mw7mZ_D0Uecy-Ub5",
    "https://youtu.be/-BjZmE2gtdo?si=cJd50LazUUSSBDrR",
    "https://youtu.be/qrxsceexTBw?si=jQtyeOspsYXzIG-5",
    "https://youtu.be/KNtJGQkC-WI?si=A5dFKXSzIY3TmiD5",
    "https://youtu.be/QYh6mYIJG2Y?si=UVm9Ht1cI3GTVDKs",
    "https://youtu.be/1ekZEVeXwek?si=FOK-7cWR9fSKJcJQ",
    "https://youtu.be/uKqRAC-JNOM?si=9jkl6NGUpUPeYQ-3",
    "https://youtu.be/SA7AIQw-7Ms?si=ow5fnsi7xeRvtN4C",
    "https://youtu.be/pE49WK-oNjU?si=kRXL3gIo-Ynngu0j",
    "https://youtu.be/Y2E71oe0aSM?si=CawfsWgmx0C9zEh3",
    "https://youtu.be/Fp_P_e1cPOE?si=366LqAAWxsVoywmL",
    "https://youtu.be/LAYgZEMMWxo?si=3xVRPfmVaPjM90dW",
    "https://youtu.be/RgKAFK5djSk?si=s5JAsveU6gPYlsi3",
    "https://youtu.be/BSwM3XR8pN4?si=CARu9pzesukM4T4p",
    "https://youtu.be/jzD_yyEcp0M?si=uOHKElD-YLNoRZGK",
    "https://youtu.be/BGyVpL2kU_Y?si=xduaAo0oLfw5tYQ6",
    "https://youtu.be/DAYszemgPxc?si=lDC7vnBwgp6ELCiw",
    "https://youtu.be/VY1eFxgRR-k?si=EeTraRxWOK7d-YCI",
    "https://youtu.be/1rVY08gRGmA?si=8Bf7tnJNlq5wLMiO",
    "https://youtu.be/l5sgIqzlPXc?si=7JV4G2b4vC5HyztS",
    "https://youtu.be/CKg4WARv_hA?si=98cMaOpTkdSCYlgp",
    "https://youtu.be/CKg4WARv_hA?si=qQnnqKpsE9tAeNAI",
    "https://youtu.be/34Na4j8AVgA?si=nvQv48iWyX_SB_JL",
    "https://youtu.be/8xg3vE8Ie_E?si=zyaCQzOE4a1qlEj6",
    "https://youtu.be/kJQP7kiw5Fk?si=zerCrddGAan-KvCc",
    "https://youtu.be/60ItHLz5WEA?si=w4bvLFLitI8ic8R5",
    "https://youtu.be/YaEG2aWJnZ8?si=6lmnTWVNhPyCO1wE",
    "https://youtu.be/nYh-n7EOtMA?si=mnn5DuzCdRogDxlE",
    "https://youtu.be/Qvd-I7lTecI?si=HSm3x5osK8gbQHNc",
    "https://youtu.be/Qvd-I7lTecI?si=GSCVRQQiAlSDoOLw",
    "https://youtu.be/iv7lcUkFVSc?si=1-zZ--wgBTeo8pUD",
    "https://youtu.be/MdhjLM-99lQ?si=rFIE8_B0ncV3JC0K",
    "https://youtu.be/6-n_szx2XRE?si=LnNi8v3wJxu93QWa",
    "https://youtu.be/DS-raAyMxl4?si=JHhrJEfc3-B_VD2P",
    "https://youtu.be/DS-raAyMxl4?si=sb2FCpBTahQEpP8k",
    "https://youtu.be/w8LcxY43N5Y?si=36s41ely90joyRDV",
    "https://youtu.be/qoq8B8ThgEM?si=VtHRPMACzHgt5uaQ",
    "https://youtu.be/clzuRgaV5dw?si=1-_78lqLUzV1Lj28",
    "https://youtu.be/A5pSnIwbpaM?si=423tXOF5dmVJiaz9",
    "https://youtu.be/dOR-yZgo1_0?si=nxk30l9gZj-Jk3Yq",
    "https://youtu.be/A5pSnIwbpaM?si=3bgApFXYlseoAMrV",
    "https://youtu.be/8MUgi5liyMU?si=e7t1P21cBowDnUtj",
    "https://youtu.be/ztPa6vkM-yY?si=DP3aOVPXBaYTemdx",
    "https://youtu.be/sRmRLJcLAEw?si=oKTeNpTTTQvq23Fc",
    "https://youtu.be/lUPltG1hb3k?si=0DyYI7Bwi_wrSs_Q",
    "https://youtu.be/fXRvluHnjxE?si=5dpUcd2IXmR4lXhA", #mast magan
    "https://youtu.be/GqR4gLsjEKc?si=3boUjC-1Yy3xd57m", #Tu har Lamha
    "https://youtu.be/gB6RIZOMY2k?si=Nncb0GFDnQYzX77s", #Ishq risk
    "https://youtu.be/FvVXaDOuaV0?si=K4TmCNy7SQ7FfBLT", #Saiyyan
    "https://youtu.be/rLR37BR88T0?si=VNqS0FkJDfNYupVe", #Tera hone lgahu
    "https://youtu.be/hHuG7FIKgtc?si=EMiOU4Dho_7ADORE", #Ishq
    "https://youtu.be/ilNt2bikxDI?si=IeGH_lLBUn9FPKec", #Tum jo mere ho
    "https://youtu.be/uSibwB2TQC4?si=1Ronpq4pTj7TrvA-", #Hale dil
    "https://youtu.be/hXh35CtnSyU?si=99GMK7kf2nXFWtXd", #Bulleya
    "https://youtu.be/1rVY08gRGmA?si=UbE-Wohsu_9vb5se", #Fairytale
    "https://youtu.be/kFfZDZeJOeE?si=zCx_AL0Jy5W34u7a",
    "https://youtu.be/JlPhR3pg0i0?si=p6D02KuNz3j5mbse",
    "https://youtu.be/3PqxT1VqyNc?si=jxWtjJAlZhF_Yh6X",
    "https://youtu.be/zWEOx7TSM6I?si=RjI_MkjaQa29bbFU",
    "https://youtu.be/A5pSnIwbpaM?si=wpkoPYUrvX4tk8xF",
    "https://youtu.be/O9B8SqE51pk?si=tlAIYWxr-uOk57qj"
    "https://youtu.be/ZzlYEprb8Ik?si=5rMtr8p5NOksoFfP",
    "https://youtu.be/-yNlgMX2LjA?si=u-hGD8wc8ldSv6br"
    ]




def download_song_and_thumbnail(url):
    ydl_opts = {
        'verbose': False,
        'ignoreerrors': True,
        # 'format': 'm4a/bestaudio/best', # for audio
        'format': 'bestvideo[ext=mp4]+bestaudio', # for video
        # 'postprocessors': [
        # {
        #     # 'key': 'FFmpegExtractAudio',
        #     # 'preferredcodec': 'mp3',
        #     # 'preferredquality' : 'best',
        # },
        # ],
        'writethumbnail': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    print("Youtube Audio Downloader : ")

    for url in urls:
        print(f"downloading from {url}")
        download_song_and_thumbnail(url)