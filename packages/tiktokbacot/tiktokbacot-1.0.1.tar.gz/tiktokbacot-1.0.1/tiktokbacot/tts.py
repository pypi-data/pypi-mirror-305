import requests
import base64

API_BASE_URL = f"https://api16-normal-v6.tiktokv.com/media/api/text/speech/invoke/"
USER_AGENT = f"com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)"

VOICE_OPTIONS = {
    "id": ["id_001"],
    "disney": ["en_us_ghostface", "en_us_chewbacca", "en_us_c3po", "en_us_stitch", "en_us_stormtrooper", "en_us_rocket"],
    "english": ["en_au_001", "en_au_002", "en_uk_001", "en_uk_003", "en_us_001", "en_us_002", "en_us_006", "en_us_007", "en_us_009", "en_us_010"],
    "europe": ["fr_001", "fr_002", "de_001", "de_002", "es_002"],
    "america": ["es_mx_002", "br_001", "br_003", "br_004", "br_005"],
    "asia": ["jp_001", "jp_003", "jp_005", "jp_006", "kr_002", "kr_003", "kr_004"],
    "singing": ["en_female_f08_salut_damour", "en_male_m03_lobby", "en_female_f08_warmy_breeze", "en_male_m03_sunshine_soon"],
    "other": ["en_male_narration", "en_male_funny", "en_female_emotional"]
}

def tiktok_tts(session_id, text, voice_category="id", voice_index=0, filename=None):
    """
    Mengubah teks menjadi suara menggunakan API TikTok.

    Args:
        session_id: Session ID TikTok yang valid.
        text: Teks yang akan diubah menjadi suara.
        voice_category: Kategori suara (default: "id").
            Pilihan: "id", "disney", "english", "europe", "america", "asia", "singing", "other".
        voice_index: Indeks suara dalam kategori (default: 0).
        filename: Nama file untuk menyimpan output audio (default: None).
            Jika None, audio tidak akan disimpan ke file, melainkan 
            dikembalikan sebagai string base64.
    
    Returns:
        str: Data audio dalam bentuk string base64 jika filename=None, 
             None jika filename diberikan.
    """
    try:
        # Mendapatkan daftar suara untuk kategori yang dipilih
        voices = VOICE_OPTIONS.get(voice_category)
        if not voices:
            print(f"Error: Kategori suara '{voice_category}' tidak valid.")
            return None

        # Memeriksa apakah indeks suara valid
        if voice_index < 0 or voice_index >= len(voices):
            print(f"Error: Indeks suara tidak valid untuk kategori '{voice_category}'.")
            return None

        # Memilih suara berdasarkan kategori dan indeks
        text_speaker = voices[voice_index]

        # Melakukan request ke API
        response = requests.post(
            f"{API_BASE_URL}?text_speaker={text_speaker}&req_text={text}&speaker_map_type=0&aid=1233",
            headers={
                'User-Agent': USER_AGENT,
                'Cookie': f'sessionid={session_id}'
            }
        )

        # Memeriksa response
        response.raise_for_status()  # Raise HTTPError untuk bad responses (4xx or 5xx)
        data = response.json()

        if data["message"] == "Couldn't load speech. Try again.":
            print("Error: Session ID tidak valid atau masalah dengan API TikTok.")
            return None 

        # Menyimpan audio ke file jika filename diberikan
        if filename:
            audio_data = base64.b64decode(data["data"]["v_str"])
            with open(filename, "wb") as out:
                out.write(audio_data)
            print(f"Berhasil! Audio disimpan di {filename}")
            return None
        else:
            # Mengembalikan data audio sebagai string base64
            return data["data"]["v_str"]

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None