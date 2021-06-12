# ngi-buster
**頭のいい人は察しなさい**
## How to use
- `git clone https://github.com/Re-taro/ngi-buster.git`を実行します
- `pipenv install`を実行します
- 別途ChromeとChromedriverがインストールされていることが前提です
>driver_path = '/usr/bin/chromedriver'
- main.pyの9行目のPATH部分をあなたのChromedriverのディレクトリに変更してください
>driver.get('https://w5.linguaporta.jp/user/seibido/index.php')
- あなたの年ではURLが変更されているかもしれません、その場合はmain.pyの16行目のURLを変更してください
- `Enter your name: `のあとにあなたのログインIDを入力ください
- `Enter your password: `のあとにあなたのログインパスワードを入力してください
- `ユニットの最初の番号を入力してください: `のあとにあなたが開始したいユニットの番号を入力してください
- `終了する番号を入力してください: `のあとにあなたが終了したいユニットの番号を入力してください
## LICENSE
MIT-LICENSE
