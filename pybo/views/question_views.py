from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        # POST로 받은 데이터로 QuestionForm 인스턴스 생성함. => 데이터를 폼으로 변환 O.
        if form.is_valid():
            question = form.save(commit=False)
            # commit=False : 데베에 저장하지 않고 폼에서 생성된 모델 인스턴스만 생성.
            question.author = request.user 
            # request.user에 로그인 상태면 User객체, 로그아웃 상태면 AnonymousUser 객체가 들어있음.
            question.create_date = timezone.now()
            # 모델 인스턴스의 필드 설정.
            question.save()
            # 데베에 저장.
            return redirect('pybo:index')
            # 페이지로 리디렉션
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
        #GET으로 올 시, 폼의 속성 값이 instance의 값으로 채워짐. => 수정화면에서 
        # 질문과 내용이 그대로 보임.-> 저장하기 누르면 POST 요청.
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권환이 없습니다.')
        return redirect('pybo:detail', question_id=question_id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)