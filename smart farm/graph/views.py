from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse
import pandas as pd
import json

class GraphView(TemplateView):
    template_name = 'graph/graph.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # CSV 파일 읽기 (상대 경로 사용)
            df = pd.read_csv('dummy_data.csv')
            # 데이터프레임을 JSON으로 변환
            context['initial_data'] = df.to_json(orient='records')
            # 컬럼 이름도 컨텍스트에 추가
            context['columns'] = list(df.columns)
        except Exception as e:
            print(f"Error reading CSV: {e}")
            context['initial_data'] = '[]'
            context['columns'] = []
        return context

class DataUpdateView(View):
    def get(self, request):
        try:
            df = pd.read_csv('dummy_data.csv')
            return JsonResponse({
                'data': df.to_dict(orient='records'),
                'columns': list(df.columns)
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=500)