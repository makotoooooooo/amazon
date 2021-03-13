from django.shortcuts import render

# Create your views here.
## 中略 ##
from django.views import generic # [2-2]追加

# [2-2] ランディングページビュー追加 ここから
class Lp(generic.TemplateView):
    template_name = 'amazon/lp.html'
# [2-2] ランディングページビュー追加 ここまで

