# sast2023 python

基础功能和streamlit的GUI界面
## 环境配置

streamlit库，详见requirement.txt

## 使用设置


约定以下参数：
--file  -f  接文章的路径    (compulsory)
--artic -a 接选用的文章标题    (optional,randomly chosen if not put in)
文章使用 JSON 存储
### 命令行版本
用户在命令行直接输入 <p><b>
```python cmdin.py -f <文件路径> (-a <文章标题>)```
</b></p>
即可，随后按照命令行提示输入相关内容
### GUI版本
用户在命令行输入 <p><b>
```streamlit run GUI.py```
</b></p>
在弹出的图形化界面中选取题库文件，并选择的文章标题，按提示填词。
<p>当且仅当所有词均填写完毕时，界面会显示填好的文章</p>