# Correctness and Impact on PyFET
In **Section 5.2**, we do a study on the correctness and impact of PyFET. In this section we give details on the dataset used. In total we use 1200 samples, out of which 300 are from the top 10 Applications to give detailed example of FET transforamtions.

## FET Examples for top 10 Applications
We give detailed transformation results for each FET (total 30) applied on one Python source file from the top 10 Applications. The files can be found as follows.

### [Rule_1_17](https://github.com/pyfet-pyc/src/tree/main/Correctness_and_Impact_PyFET/Rule_1_17):
- FET examples for the first 17 FET rules for one Python source file in each of the top 10 Application.
### [Rule_18_30](https://github.com/pyfet-pyc/src/tree/main/Correctness_and_Impact_PyFET/Rule_18_30):
- FET examples for the last 14 FET rules for one Python source file in each of the top 10 Application.

## Remainder Samples used for Section 5.2.

### [Addtional_900_samples](https://github.com/pyfet-pyc/src/tree/main/Correctness_and_Impact_PyFET/Addtional_900_samples):
- Remainder 900 sample transformations used in the study.

## Details of 100 Python Projects used in Evaluation

This page contains the list top 100 Python projects used in evaluation in detail, which is mentioned in 5. Evaluation, 5.2. Correctness and Impact of PyFET. We summarized the related contents as a below table. 
We download top 100 Python projects based on popularity (# of stars) from GitHub (out of 2M+) for our ground truth study (14,949 Python source files).

- 100 applications are listed in order of popularity (the number of stars).
- **Title**: The name of system or Github repository (⭐ means the top 10 applications used for FET examples). 
  - We use `---` as a title instead of the original title as it is considered inappropriate (e.g., slang)
- **Forks**: The number of forks.
- **Star**: The number of star which means the popularity in GitHub.
- **Size**: The size (byte) of the project
- **SLOC**: SLOC of the project
- **\# of py files**: The number of Python files (*.py) in the project
- **\# of functions**: Among Python files (*.py), the number of functions
- **SLOC (py)**: SLOC of Python files (*.py)

| Id  | Title                                | Forks  | Star    | Size    | SLOC      | # of py files | # of functions | SLOC (py) | Repo                                                                      |
|----:|--------------------------------------|-------:|--------:|--------:|----------:|--------------:|---------------:|----------:|---------------------------------------------------------------------------|
| 1   | system-design-primer                 | 33,689 | 185,170 | 13,588  | 10,375    | 15            | 148            | 655       | [Link](https://github.com/donnemartin/system-design-primer)               |
| 2   | ---                                  | 21,383 | 131,641 | 140     | 1,197     | 1             | 2              | 45        | [Link](https://github.com/vinta/awesome-python)                           |
| 3   | Python-100-Days                      | 45,861 | 120,143 | 97,876  | 40,303    | 189           | 439            | 4,034     | [Link](https://github.com/jackfrued/Python-100-Days)                      |
| 4   | youtube-dl ⭐                         | 7,884  | 111,111 | 8,112   | 131,841   | 870           | 3,377          | 124,827   | [Link](https://github.com/ytdl-org/youtube-dl)                            |
| 5   | ---                                  | 3,221  | 71,858  | 2,964   | 11,105    | 392           | 1,375          | 9,893     | [Link](https://github.com/nvbn/thefuck)                                   |
| 6   | keras ⭐                              | 19,126 | 55,520  | 18,748  | 190,114   | 630           | 11,337         | 180,444   | [Link](https://github.com/keras-team/keras)                               |
| 7   | ansible ⭐                            | 22,052 | 53,615  | 52,256  | 282,440   | 1,060         | 7,288          | 103,136   | [Link](https://github.com/ansible/ansible)                                |
| 8   | face_recognition                     | 12,340 | 45,020  | 15,504  | 3,563     | 29            | 75             | 1,436     | [Link](https://github.com/ageitgey/face_recognition)                      |
| 9   | ---                                  | 2,031  | 42,530  | 264     | 2,664     | 2             | 1              | 19        | [Link](https://github.com/minimaxir/big-list-of-naughty-strings)          |
| 10  | localstack ⭐                         | 3,109  | 41,821  | 17,796  | 166,613   | 380           | 4,861          | 62,114    | [Link](https://github.com/localstack/localstack)                          |
| 11  | PayloadsAllTheThings                 | 10,483 | 38,501  | 11,140  | 24,844    | 28            | 89             | 2,868     | [Link](https://github.com/swisskyrepo/PayloadsAllTheThings)               |
| 12  | rich ⭐                               | 1,270  | 38,211  | 19,896  | 40,741    | 175           | 1,581          | 25,536    | [Link](https://github.com/Textualize/rich)                                |
| 13  | openpilot ⭐                          | 6,428  | 35,236  | 178,608 | 137,908   | 329           | 2,086          | 31,191    | [Link](https://github.com/commaai/openpilot)                              |
| 14  | pandas ⭐                             | 14,597 | 34,356  | 54,296  | 463,461   | 886           | 16,455         | 226,219   | [Link](https://github.com/pandas-dev/pandas)                              |
| 15  | d2l-zh                               | 7,742  | 33,274  | 70,168  | 132,635   | 9             | 626            | 5,371     | [Link](https://github.com/d2l-ai/d2l-zh)                                  |
| 16  | shadowsocks                          | 19,315 | 33,193  | 8       | 0         | 0             | 0              | 0         | [Link](https://github.com/shadowsocks/shadowsocks)                        |
| 17  | Deep-Learning-Papers-Reading-Roadmap | 6,947  | 32,660  | 52      | 286       | 1             | 6              | 114       | [Link](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) |
| 18  | XX-Net ⭐                             | 7,793  | 31,275  | 42,116  | 307,500   | 939           | 21,424         | 258,724   | [Link](https://github.com/XX-net/XX-Net)                                  |
| 19  | cheat.sh ⭐                           | 1,488  | 29,529  | 6,412   | 6,400     | 40            | 269            | 3,455     | [Link](https://github.com/chubin/cheat.sh)                                |
| 20  | python-cheatsheet                    | 5,381  | 29,449  | 12,416  | 32,139    | 5             | 22             | 209       | [Link](https://github.com/gto76/python-cheatsheet)                        |
| 21  | certbot                              | 3,230  | 29,023  | 9,516   | 56,918    | 214           | 3,282          | 30,916    | [Link](https://github.com/certbot/certbot)                                |
| 22  | jieba ⭐                              | 6,571  | 28,811  | 51,724  | 919,179   | 47            | 70             | 98,818    | [Link](https://github.com/fxsjy/jieba)                                    |
| 23  | black                                | 1,785  | 28,340  | 6,176   | 108,987   | 160           | 1,335          | 103,016   | [Link](https://github.com/psf/black)                                      |
| 24  | yt-dlp                               | 2,169  | 27,584  | 10,528  | 170,054   | 1,052         | 4,697          | 157,970   | [Link](https://github.com/yt-dlp/yt-dlp)                                  |
| 25  | HanLP                                | 7,148  | 26,274  | 5,020   | 41,371    | 323           | 2,480          | 31,946    | [Link](https://github.com/hankcs/HanLP)                                   |
| 26  | Python                               | 10,973 | 25,719  | 39,664  | 211,516   | 486           | 1,390          | 24,368    | [Link](https://github.com/geekcomputers/Python)                           |
| 27  | Detectron                            | 5,454  | 25,219  | 5,296   | 18,776    | 86            | 626            | 11,740    | [Link](https://github.com/facebookresearch/Detectron)                     |
| 28  | YouCompleteMe                        | 2,770  | 24,041  | 1,748   | 18,119    | 52            | 869            | 10,105    | [Link](https://github.com/ycm-core/YouCompleteMe)                         |
| 29  | sqlmap                               | 4,888  | 23,869  | 12,624  | 68,800    | 229           | 2,174          | 41,277    | [Link](https://github.com/sqlmapproject/sqlmap)                           |
| 30  | pipenv                               | 1,749  | 23,069  | 24,496  | 223,177   | 541           | 7,344          | 146,069   | [Link](https://github.com/pypa/pipenv)                                    |
| 31  | PaddleOCR                            | 4,704  | 22,974  | 141,400 | 104,272   | 249           | 1,883          | 46,255    | [Link](https://github.com/PaddlePaddle/PaddleOCR)                         |
| 33  | python-fire                          | 1,307  | 22,616  | 636     | 7,225     | 56            | 688            | 6,171     | [Link](https://github.com/google/python-fire)                             |
| 32  | httpie                               | 3,683  | 22,255  | 1,316   | 7,057     | 15            | 201            | 2,153     | [Link](https://github.com/httpie/httpie)                                  |
| 34  | ItChat                               | 5,250  | 22,248  | 2,816   | 18,229    | 106           | 1,002          | 12,721    | [Link](https://github.com/littlecodersh/ItChat)                           |
| 35  | MockingBird                          | 3,228  | 22,135  | 122,856 | 30,461    | 118           | 588            | 9,011     | [Link](https://github.com/babysor/MockingBird)                            |
| 36  | redash                               | 3,720  | 21,306  | 12,672  | 86,553    | 209           | 1,747          | 22,242    | [Link](https://github.com/getredash/redash)                               |
| 37  | algorithms                           | 4,331  | 21,178  | 2,292   | 13,830    | 367           | 1,397          | 12,344    | [Link](https://github.com/keon/algorithms)                                |
| 38  | ray                                  | 3,673  | 21,064  | 108,332 | 607,554   | 1,961         | 20,850         | 297,985   | [Link](https://github.com/ray-project/ray)                                |
| 39  | hosts                                | 1,835  | 21,023  | 97,564  | 11,790    | 4             | 186            | 2,604     | [Link](https://github.com/StevenBlack/hosts)                              |
| 40  | CheatSheetSeries                     | 3,005  | 20,996  | 18,092  | 19,885    | 5             | 3              | 221       | [Link](https://github.com/OWASP/CheatSheetSeries)                         |
| 41  | numpy                                | 7,050  | 20,795  | 37,200  | 434,212   | 593           | 10,712         | 124,115   | [Link](https://github.com/numpy/numpy)                                    |
| 42  | glances                              | 1,304  | 20,720  | 13,516  | 53,943    | 112           | 999            | 12,729    | [Link](https://github.com/nicolargo/glances)                              |
| 43  | NLP-progress                         | 3,473  | 20,566  | 1,020   | 4,240     | 1             | 13             | 269       | [Link](https://github.com/sebastianruder/NLP-progress)                    |
| 44  | cascadia-code                        | 679    | 20,357  | 75,504  | 898       | 1             | 13             | 514       | [Link](https://github.com/microsoft/cascadia-code)                        |
| 45  | mmdetection                          | 7,409  | 20,222  | 46,072  | 113,894   | 1,095         | 2,610          | 84,143    | [Link](https://github.com/open-mmlab/mmdetection)                         |
| 46  | spleeter                             | 2,198  | 19,884  | 2,036   | 3,087     | 22            | 115            | 2,017     | [Link](https://github.com/deezer/spleeter)                                |
| 47  | streamlit                            | 1,768  | 19,685  | 49,144  | 539,642   | 403           | 2,926          | 33,103    | [Link](https://github.com/streamlit/streamlit)                            |
| 48  | GFPGAN                               | 3,010  | 19,548  | 6,536   | 3,730     | 21            | 117            | 2,922     | [Link](https://github.com/TencentARC/GFPGAN)                              |
| 49  | pytorch-image-models                 | 3,195  | 19,332  | 5,452   | 67,972    | 196           | 3,113          | 36,921    | [Link](https://github.com/rwightman/pytorch-image-models)                 |
| 50  | macOS-Security-and-Privacy-Guide     | 1,389  | 19,252  | 684     | 3,015     | 1             | 6              | 69        | [Link](https://github.com/drduh/macOS-Security-and-Privacy-Guide)         |
| 51  | locust                               | 2,471  | 19,153  | 3,336   | 22,021    | 88            | 1,395          | 16,755    | [Link](https://github.com/locustio/locust)                                |
| 52  | jax                                  | 1,740  | 19,027  | 20,708  | 160,606   | 304           | 11,506         | 109,187   | [Link](https://github.com/google/jax)                                     |
| 53  | python-telegram-bot                  | 4,165  | 18,989  | 7,108   | 55,458    | 325           | 3,961          | 52,687    | [Link](https://github.com/python-telegram-bot/python-telegram-bot)        |
| 54  | vnpy                                 | 7,344  | 18,660  | 2,208   | 9,883     | 31            | 322            | 3,594     | [Link](https://github.com/vnpy/vnpy)                                      |
| 55  | pytorch-CycleGAN-and-pix2pix         | 5,361  | 17,831  | 8,028   | 2,849     | 32            | 169            | 1,941     | [Link](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)           |
| 56  | magenta                              | 3,634  | 17,708  | 26,612  | 53,434    | 278           | 2,352          | 38,080    | [Link](https://github.com/magenta/magenta)                                |
| 57  | labelImg                             | 5,451  | 17,669  | 7,216   | 8,021     | 28            | 286            | 3,332     | [Link](https://github.com/tzutalin/labelImg)                              |
| 58  | Awesome-Linux-Software               | 1,779  | 17,554  | 1,188   | 6,596     | 4             | 4              | 169       | [Link](https://github.com/luong-komorebi/Awesome-Linux-Software)          |
| 59  | fairseq                              | 4,577  | 17,332  | 22,432  | 147,524   | 707           | 6,488          | 109,589   | [Link](https://github.com/facebookresearch/fairseq)                       |
| 60  | dash                                 | 1,720  | 16,721  | 32,344  | 282,080   | 223           | 1,811          | 26,812    | [Link](https://github.com/plotly/dash)                                    |
| 61  | reddit                               | 2,896  | 16,113  | 16,184  | 162,483   | 265           | 5,467          | 62,954    | [Link](https://github.com/reddit-archive/reddit)                          |
| 62  | zulip                                | 5,419  | 16,029  | 77,144  | 732,356   | 949           | 7,488          | 152,517   | [Link](https://github.com/zulip/zulip)                                    |
| 63  | matplotlib                           | 6,414  | 15,710  | 75,764  | 568,671   | 849           | 9,215          | 122,211   | [Link](https://github.com/matplotlib/matplotlib)                          |
| 64  | PythonRobotics                       | 5,056  | 15,567  | 9,964   | 21,288    | 188           | 1,221          | 18,334    | [Link](https://github.com/AtsushiSakai/PythonRobotics)                    |
| 65  | proxy\_pool                          | 4,163  | 15,524  | 300     | 1,707     | 31            | 163            | 1,165     | [Link](https://github.com/jhao104/proxy\_pool)                            |
| 66  | EasyOCR                              | 2,126  | 15,142  | 319,220 | 7,732     | 36            | 255            | 6,024     | [Link](https://github.com/JaidedAI/EasyOCR)                               |
| 67  | kitty                                | 720    | 15,064  | 19,808  | 202,333   | 157           | 2,918          | 34,592    | [Link](https://github.com/kovidgoyal/kitty)                               |
| 68  | python-spider                        | 5,574  | 15,003  | 1,668   | 4,457     | 68            | 216            | 3,638     | [Link](https://github.com/Jack-Cherish/python-spider)                     |
| 69  | jina                                 | 1,929  | 14,999  | 42,244  | 57,240    | 227           | 1,765          | 27,464    | [Link](https://github.com/jina-ai/jina)                                   |
| 70  | avatarify-python                     | 2,278  | 14,958  | 5,060   | 2,098     | 9             | 80             | 1,101     | [Link](https://github.com/alievk/avatarify-python)                        |
| 71  | ungoogled-chromium                   | 684    | 14,810  | 3,936   | 3,584     | 28            | 215            | 2,983     | [Link](https://github.com/ungoogled-software/ungoogled-chromium)          |
| 72  | kivy                                 | 2,892  | 14,734  | 34,788  | 90,949    | 412           | 3,606          | 40,609    | [Link](https://github.com/kivy/kivy)                                      |
| 73  | prophet                              | 4,229  | 14,601  | 24,744  | 13,531    | 16            | 179            | 4,249     | [Link](https://github.com/facebook/prophet)                               |
| 74  | faker                                | 1,627  | 14,376  | 11,424  | 291,172   | 63            | 1,561          | 77,335    | [Link](https://github.com/joke2k/faker)                                   |
| 75  | wechat\_jump\_game                   | 4,463  | 13,881  | 10,580  | 2,205     | 21            | 100            | 1,749     | [Link](https://github.com/wangshub/wechat\_jump\_game)                    |
| 76  | autojump                             | 650    | 13,860  | 324     | 3,542     | 10            | 215            | 2,420     | [Link](https://github.com/wting/autojump)                                 |
| 77  | d2l-en                               | 3,166  | 13,829  | 127,084 | 188,953   | 6             | 790            | 5,980     | [Link](https://github.com/d2l-ai/d2l-en)                                  |
| 78  | ArchiveBox                           | 790    | 13,717  | 2,248   | 18,111    | 108           | 417            | 8,460     | [Link](https://github.com/ArchiveBox/ArchiveBox)                          |
| 79  | neural-networks-and-deep-learning    | 6,060  | 13,539  | 24,060  | 1,623     | 26            | 111            | 1,571     | [Link](https://github.com/mnielsen/neural-networks-and-deep-learning)     |
| 80  | fabric                               | 1,889  | 13,486  | 884     | 6,994     | 28            | 418            | 3,053     | [Link](https://github.com/fabric/fabric)                                  |
| 81  | Shadowrocket-ADBlock-Rules           | 2,226  | 13,428  | 5,232   | 494       | 5             | 11             | 309       | [Link](https://github.com/h2y/Shadowrocket-ADBlock-Rules)                 |
| 82  | recommenders                         | 2,362  | 13,479  | 7,136   | 41,970    | 154           | 1,229          | 25,129    | [Link](https://github.com/microsoft/recommenders)                         |
| 83  | gensim                               | 4,234  | 13,302  | 97,064  | 87,998    | 177           | 2,168          | 26,369    | [Link](https://github.com/RaRe-Technologies/gensim)                       |
| 84  | learn-python                         | 2,095  | 12,886  | 456     | 1,974     | 59            | 139            | 1,237     | [Link](https://github.com/trekhleb/learn-python)                          |
| 85  | imgaug                               | 2,306  | 12,732  | 7,996   | 100,070   | 146           | 8,297          | 93,354    | [Link](https://github.com/aleju/imgaug)                                   |
| 86  | baselines                            | 4,344  | 12,730  | 6,520   | 34,085    | 11            | 902            | 10,137    | [Link](https://github.com/openai/baselines)                               |
| 88  | stylegan                             | 2,941  | 12,639  | 2,016   | 3,990     | 25            | 294            | 3,805     | [Link](https://github.com/NVlabs/stylegan)                                |
| 87  | DeDRM\_tools                         | 1,197  | 12,567  | 3,008   | 7,578     | 68            | 326            | 6,699     | [Link](https://github.com/apprenticeharper/DeDRM\_tools)                  |
| 89  | facenet                              | 4,735  | 12,563  | 2,232   | 25,622    | 57            | 1,244          | 23,177    | [Link](https://github.com/davidsandberg/facenet)                          |
| 90  | pyecharts                            | 2,685  | 12,475  | 1,544   | 25,344    | 104           | 443            | 8,629     | [Link](https://github.com/pyecharts/pyecharts)                            |
| 91  | OpenBBTerminal                       | 1,351  | 12,383  | 271,604 | 2,158,414 | 664           | 3,442          | 97,773    | [Link](https://github.com/OpenBB-finance/OpenBBTerminal)                  |
| 92  | ChatterBot                           | 4,096  | 12,361  | 5,516   | 16,226    | 114           | 646            | 8,378     | [Link](https://github.com/gunthercox/ChatterBot)                          |
| 93  | the-gan-zoo                          | 2,392  | 12,299  | 992     | 1,084     | 1             | 4              | 57        | [Link](https://github.com/hindupuravinash/the-gan-zoo)                    |
| 94  | wagtail                              | 2,660  | 12,267  | 54,556  | 435,806   | 609           | 5,803          | 86,456    | [Link](https://github.com/wagtail/wagtail)                                |
| 95  | wtfpython-cn                         | 2,064  | 12,263  | 360     | 1,947     | 1             | 1              | 6         | [Link](https://github.com/leisurelicht/wtfpython-cn)                      |
| 96  | GitHub520                            | 1,387  | 12,118  | 1,236   | 329       | 1             | 7              | 123       | [Link](https://github.com/521xueweihan/GitHub520)                         |
| 97  | mlflow                               | 2,791  | 12,117  | 39,996  | 261,965   | 481           | 5,725          | 80,209    | [Link](https://github.com/mlflow/mlflow)                                  |
| 98  | mackup                               | 880    | 12,102  | 2,648   | 3,060     | 12            | 86             | 1,076     | [Link](https://github.com/lra/mackup)                                     |
| 99  | loguru                               | 531    | 12,063  | 2,052   | 12,657    | 146           | 1,274          | 10,863    | [Link](https://github.com/Delgan/loguru)                                  |
| 100 | speedtest-cli                        | 1,751  | 12,018  | 128     | 544       | 3             | 72             | 340       | [Link](https://github.com/sivel/speedtest-cli)                            |
