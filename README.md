# Double Clap Detection 👏

> Trigger actions with just two claps — real-time audio pattern detection using Python.

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![PyAudio](https://img.shields.io/badge/PyAudio-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)

---

## 🔍 About

This project listens to your microphone in real-time and detects a **double clap pattern**. When detected, it can trigger custom actions — making it a fun, hands-free control system using just sound.

---

## ✨ Features

- 🎙️ Real-time audio input via microphone
- 👏 Detects double clap pattern accurately
- ⚡ Trigger custom actions on detection
- 🔇 Filters out background noise

---

## 🛠️ Technologies Used

| Library | Purpose |
|---|---|
| Python | Core language |
| PyAudio | Microphone input & audio streaming |
| NumPy | Audio signal processing |
| OpenCV | Visual feedback (optional) |

---

## 📁 Project Structure

```
Double-Clap-Detection/
│
├── main.py           → Main detection program
└── requirements.txt  → Dependencies
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/tanasviattri5075-tech/Double-Clap-Detection.git
cd Double-Clap-Detection
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the project**
```bash
python main.py
```

---

## 🎮 How It Works

1. Microphone listens for audio input continuously
2. Audio signal is analyzed for sharp amplitude spikes (claps)
3. If two spikes are detected within a short time window → **double clap confirmed**
4. Configured action is triggered 🎉

---

## 🔮 Future Improvements

- [ ] Triple clap detection
- [ ] Adjustable sensitivity settings
- [ ] Map different clap patterns to different actions
- [ ] GUI for configuration

---

## 👩‍💻 Author

**Tanasvi Attri**  
B.Tech — ECM | Jaypee Institute of Information Technology  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/tanasvi-attri-68384b35b)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:tanasvi.attri.5075@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/tanasviattri5075-tech)

