# Film Assist
Film Assist is a macOS application for film creators to handle routine works.

## ⚙️ Features
- Convert Subtitle Files between SRT and Excel

## 🛠 Setup for Development

#### Setup Python3 & Virtualenv
Update Homebrew (Optional)
```bash
brew update
```

Install Python3
```bash
brew install python3
```

Install Virtualenv
```bash
pip3 install virtualenv
```

Go to Project folder
```bash
cd <project-folder-path>
```

Create Virtualenv and Activate
```bash
virtualenv -p python3 venv
source venv/bin/activate
```

Install Python Modules
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 💻 Developing Environment
#### System
- macOS Big Sur 11.6
- Homebrew (https://brew.sh/)

#### Python
- Python 3.9.10 (https://www.python.org/)
- virtualenv 20.4.2 (https://virtualenv.pypa.io/)

#### Python Modules (requirements.txt)
- pywebview == 3.5 # https://pypi.org/project/pywebview/
- pyinstaller == 4.9  # https://pypi.org/project/pyinstaller/
- Flask == 2.0.2 # https://pypi.org/project/Flask/
- XlsxWriter == 3.0.2 # https://pypi.org/project/XlsxWriter/
- srt == 3.5.1 # https://pypi.org/project/srt/
- timecode == 1.3.1 # https://pypi.org/project/timecode/

## ⚖️ License
© 2022 Addie Liu (liuaddie@gmail.com)

**GNU Lesser General Public License (LGPL) v3.0:** Addie Liu distributes one or more Open Source Components with the Software, which either operates as distinct processes that run in parallel with the Software or are dynamic libraries that are interacted with by the Software at runtime under the LGPL v3.0. A copy of the GNU Lesser General Public License v3.0 may be found at https://www.gnu.org/licenses/lgpl-3.0.html.
