# 🎵 K-Tube Player (YouTube គ្មានពាណិជ្ជកម្ម & ចាក់ពេលបិទអេក្រង់)

កម្មវិធីចាក់ចម្រៀង និងវីដេអូ YouTube ដែលមានល្បឿនលឿន គ្មានពាណិជ្ជកម្មរំខាន (No Ads) និងអាចចាក់បន្តពេលបិទអេក្រង់ទូរស័ព្ទ (Screen-Off Background Playback) ដោយសន្សំសំចៃថ្ម និង Internet Data រហូតដល់ 90%។

---

## ✨ លក្ខណៈពិសេសចម្បង (Key Features)

1. **គ្មានពាណិជ្ជកម្ម (100% Ad-Free)**
   - គ្មានពាណិជ្ជកម្មកាត់ផ្តាច់នៅដើមវីដេអូ កណ្តាលវីដេអូ ឬផ្ទាំង Pop-up ឡើយ។
2. **ចាក់ពេលបិទអេក្រង់ទូរស័ព្ទ (Screen-Off / Background Playback)**
   - បំពាក់ដោយ **Web MediaSession API** និង Audio Stream ដោយផ្ទាល់។
   - ពេលស្តាប់លើទូរស័ព្ទ (iOS ឬ Android) អ្នកអាចចុចបិទអេក្រង់ ឬដាក់ក្នុងហោប៉ៅ ដោយបទចម្រៀងនៅតែបន្តឮយ៉ាងរលូន។
   - បង្ហាញផ្ទាំងបញ្ជា (Lock Screen Controls) លើអេក្រង់ទូរស័ព្ទពេលបិទអេក្រង់ (Play, Pause, Skip, ឈ្មោះបទចម្រៀង និងរូបភាព Cover)។
3. **របៀបពីរសម្បូរបែប (Dual Playback Modes)**
   - 🎧 **Audio Mode (Screen-Off Mode)**: ទាញយកតែសំឡេងកម្រិតខ្ពស់ AAC 128kbps, ដើរលឿនបំផុត, សន្សំថ្ម និងទិន្នន័យ 90%។
   - 🎬 **Video Mode**: មើលវីដេអូច្បាស់កម្រិត HD គ្មានពាណិជ្ជកម្ម។
4. **ស្វែងរកលឿន & ស្វ័យប្រវត្តិតាមការវាយអក្សរ (Fast Search & Autocomplete)**
   - គាំទ្រការស្វែងរកជាភាសាខ្មែរ និងអង់គ្លេស។
   - មានប្រព័ន្ធទស្សន៍ទាយពាក្យស្វែងរក (Suggestions) ភ្លាមៗ។
5. **បញ្ជីចាក់ & ពេញនិយម (Playlists & Trending)**
   - ផ្តល់ជូនផ្ទាំងបទចម្រៀងខ្មែរពេញនិយម, Top Hits ពិភពលោក, Lofi & Chill, Podcasts, និង Acoustic។
   - ប្រព័ន្ធ Queue បន្តបន្ទាប់, Shuffle (ចាក់ចៃដន្យ), Repeat (ចាក់ឡើងវិញ)។
   - រក្សាទុកបទចម្រៀងដែលចូលចិត្ត (Favorites)។
6. **គាំទ្រ PWA ដំឡើងជា App លើទូរស័ព្ទ (Installable App)**
   - អាចដំឡើងទៅលើទូរស័ព្ទ Android និង iPhone ដូច App ធម្មតា ដោយគ្រាន់តែចុច "Add to Home screen"។

---

## 🚀 របៀបដំណើរការ (How to Run)

### ជម្រើសទី ១៖ ចុចបើកភ្លាមៗ (Windows 1-Click)
គ្រាន់តែចុចទ្វេដង (Double Click) លើឯកសារ៖
```
start.bat
```
វានឹងបើកផ្ទាំងកម្មវិធីក្នុង Browser ដោយស្វ័យប្រវត្តិ។

### ជម្រើសទី ២៖ ដំណើរការតាម Terminal / Command Line
```powershell
python -m pip install -r requirements.txt
python server.py
```
បន្ទាប់មកបើក Browser ទៅកាន់:
- **កុំព្យូទ័រ (Local PC)**: [http://localhost:8000](http://localhost:8000)
- **ទូរស័ព្ទ (Phone/Tablet)**: ស្កេន QR Code ដែលបង្ហាញលើអេក្រង់ ឬវាយលេខ IP ដូចជា `http://192.168.x.x:8000`

---

## 📱 របៀបប្រើលើទូរស័ព្ទឱ្យចាក់ឮពេលបិទអេក្រង់ (Mobile Background Playback Guide)

1. ភ្ជាប់ទូរស័ព្ទទៅកាន់ **Wi-Fi តែមួយ** ជាមួយកុំព្យូទ័ររបស់អ្នក។
2. បើក Browser លើកុំព្យូទ័រ ចុចប៊ូតុង **"ប្រើលើទូរស័ព្ទ"** ដើម្បីមើល **QR Code**។
3. យកកាមេរ៉ាទូរស័ព្ទស្កេន QR Code នោះដើម្បីបើក K-Tube Player។
4. **របៀបចាក់ពេលបិទអេក្រង់**៖
   - ជ្រើសរើសរបៀប **"Audio Mode (Screen Off)"** (រូបកាស 🎧)។
   - ចុចចាក់បទចម្រៀងដែលអ្នកចូលចិត្ត។
   - អ្នកអាចចុចបិទអេក្រង់ទូរស័ព្ទ (Lock screen) បានភ្លាមៗ ចម្រៀងនឹងនៅតែបន្តចាក់ឮ ហើយអ្នកអាចចុច Play/Pause ឬប្តូរបទពីលើ Lock screen បានដោយសេរី!
5. **របៀបដាក់ជា App លើអេក្រង់ទូរស័ព្ទ (Add to Home screen)**៖
   - **Android (Chrome)**: ចុចសញ្ញាចុច ៣ (Menu) នៅខាងលើស្តាំ -> ជ្រើសរើស **"Install app"** ឬ **"Add to Home screen"**។
   - **iPhone (Safari)**: ចុចប៊ូតុង Share (សញ្ញាព្រួញឡើងលើ) -> ជ្រើសរើស **"Add to Home Screen"**។

---

## 🛠️ បច្ចេកវិទ្យាប្រើប្រាស់ (Tech Stack)
- **Backend**: Python 3.12, FastAPI (High-performance Async Web Server), Uvicorn, HTTPX Chunked Stream Proxy.
- **Extractor**: yt-dlp (Node JS runtime + Static FFmpeg).
- **Frontend**: Responsive Tailwind CSS, Phosphor Icons, Web MediaSession API, Service Worker (PWA), LocalStorage.

