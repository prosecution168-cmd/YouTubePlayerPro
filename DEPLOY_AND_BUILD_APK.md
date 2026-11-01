# ការណែនាំបង្កើត APK សម្រាប់ Android (YouTube Player Pro)

ឯកសារកូដសម្រាប់ Deploy ត្រូវបានរៀបចំរួចជាស្រេចនៅក្នុងកញ្ចប់៖
👉 `YouTubePlayerPro_Source_Cloud.zip`

---

## ជំហានទី ១៖ ដាក់ Server ដំណើរការ ២៤/៧ លើ Render.com (ឥតគិតថ្លៃ ១០០%)
1. ចូលទៅកាន់គេហទំព័រ [https://render.com](https://render.com) រួចចុច **Sign Up** (អាច Sign in ដោយប្រើគណនី Google ឬ GitHub)
2. ចុចលើប៊ូតុង **"New +"** នៅខាងលើស្តាំ ➔ ជ្រើសរើស **"Web Service"**
3. Upload ឬជ្រើសរើស Repository នៃកូដរបស់អ្នក (ឬបង្កើតតាម GitHub ដោយ Upload `YouTubePlayerPro_Source_Cloud.zip`)
4. កំណត់ដូចខាងក្រោម៖
   * **Name:** `youtube-player-pro`
   * **Language/Runtime:** `Python 3`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `uvicorn server:app --host 0.0.0.0 --port $PORT`
   * **Instance Type:** `Free`
5. ចុច **"Create Web Service"**
6. រង់ចាំប្រហែល ១ ទៅ ២ នាទី លោកអ្នកនឹងទទួលបាន Link អនឡាញផ្លូវការមួយ ដូចជា៖
   👉 `https://youtube-player-pro.onrender.com`

---

## ជំហានទី ២៖ វេចខ្ចប់ Link អនឡាញជាឯកសារ APK ផ្លូវការ
1. ចូលទៅកាន់គេហទំព័រផ្លូវការរបស់ Microsoft PWA Builder: [https://www.pwabuilder.com](https://www.pwabuilder.com)
2. យក Link អនឡាញដែលទើបតែទទួលបានពី Render (ឧ. `https://youtube-player-pro.onrender.com`) មកបិទភ្ជាប់ (Paste) ក្នុងប្រអប់ រួចចុច **Start**
3. ប្រព័ន្ធនឹងពិនិត្យមើល `manifest.json` និង `icons` ដោយស្វ័យប្រវត្តិ (ឃើញពិន្ទុពេញ ១០០%)
4. ចុចលើប៊ូតុង **"Package for Stores"**
5. នៅកន្លែង **Android** ចុចលើប៊ូតុង **"Generate Package"**
6. ជ្រើសរើសយក **"Download APK"**

---

## ជំហានទី ៣៖ ទាញយក និងដំឡើងលើទូរស័ព្ទ Android
1. ផ្ញើ File `YouTubePlayerPro.apk` ចូលទូរស័ព្ទ (តាមរយៈ Telegram, Google Drive, ឬទាញយកផ្ទាល់លើទូរស័ព្ទ)
2. ចុចលើ File `.apk` នោះ
3. ប្រសិនបើទូរស័ព្ទសួរ "Allow from this source" សូមចុច **Allow (អនុញ្ញាត)**
4. ចុច **"Install" (ដំឡើង)**
5. រួចរាល់ជាស្ថាពរ! App នឹងបង្ហាញនៅលើអេក្រង់ដើមទូរស័ព្ទ អាចបើកស្តាប់តន្ត្រី គ្មានពាណិជ្ជកម្ម និងចាក់ពេលបិទអេក្រង់បានគ្រប់ទីកន្លែង ២៤ម៉ោង!

