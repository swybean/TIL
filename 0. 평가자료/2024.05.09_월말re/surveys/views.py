from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Topic, Question, Choice, Answer
from .serializers import (
    TopicListSerializer,
    TopicDetailSerializer,
    TopicSerializer,
    QuestionListSerializer,
    QuestionSerializer,
    QuestionDetailSerializer,
    ChoiceListSerializer,
    ChoiceSerializer,
    AnswerListSerializer,
    AnswerSerializer,
    AnswerUpdateSerializer
)


@api_view(['GET', 'POST'])
def topic_create_list(request):
    if request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        topics = get_list_or_404(Topic)
        serializer = TopicListSerializer(topics, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail_update_delete(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)

    if request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        topic.delete()
        return Response({'topic': f'{topic_pk} deleted'}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = TopicDetailSerializer(topic)
        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
def question_create_list(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(topic=topic)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        questions = topic.question_set.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)
    
# 문제 5. DELETE 동작 후 적절한 status code 응답하기
@api_view(['GET', 'PUT', 'DELETE'])
def question_detail_update_delete(request, topic_pk, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    if request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        question.delete()
        return Response({'question': f'{question_pk} deleted'}, status=status.HTTP_204_NO_CONTENT)
        ### status code는 Response에 붙여야 한다.
        ### DELETE는 코드명을 NO_CONTENT를 사용해야 한다.
    else:
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)


# 문제 6. 좋아요 증가시키고 저장하기
# 응답은 좋아요 개수를 리턴 (필드 이름은 'good_question' 으로 한다.)
@api_view(['POST'])
def question_good(request, topic_pk, question_pk):
    good_question = Question.objects.get(pk=question_pk)
    good_question.good_question += 1
    good_question.save()
    return Response({'good_question': f'{good_question.good_question}' })
    ### 필드이름을 good_question으로 설정하라고 해서 설정한다.
    ### Question 모델에서 pk가 같은 것을 good_question으로 할당해준다.
    ### 그리고 좋아요 개수 이름도 good_question이니까 good_question.good_question의 개수를 += 1해준다.
    ### DB에 저장될 수 있도록 good_question.save()를 해준다.


# 문제 7. 특정 question의 choice만 응답 데이터로 전달하기
# 문제 8. choice 생성 시 Not NULL 에러 해결하기
@api_view(['GET', 'POST'])
def choice_create_list(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    
    if request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(question=question)
            ### 외래키가 NULL 상태 그대로 생성하려고하면 에러가 발생한다.
            ### 특정 테이블 외래키에도 따로 저장되도록 save()안에 question=question을 해줘야 한다.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        choices = Choice.objects.filter(question=question)
        ### filter를 이용한다. all을 사용하면 전부다 가져오니까
        ### question= question을 사용해서 위에서 정의한 question과 Choise 모델의 외래키 question이
        ### 같은 choice만 걸러서 가져온다.
        serializer = ChoiceListSerializer(choices, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
def choice_detail_update_delete(request, question_pk, choice_pk):
    choice = get_object_or_404(Choice, pk=choice_pk)

    if request.method == 'PUT':
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        choice.delete()
        return Response({'choice': f'{choice_pk} deleted'}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

# 문제 9. 답변 리스트를 GET 요청시 에러 발생 해결하기
# 문제 10. 답변 생성 기능 구현하기 (AnswerSerializer 사용)
@api_view(['GET', 'POST'])
def answer_create_list(request, choice_pk):
    choice = get_object_or_404(Choice, pk=choice_pk)

    if request.method == 'POST':
        pass
    else:
        answers = choice.answer_set.all()
        serializer = AnswerListSerializer(answers, many=True)
        ### 답변 '리스트'니까 여러개를 불러오는 것이다. 따라서 many=True를 설정해줘야 한다.
        
        return Response(serializer.data)
    

# 문제 11. Answer의 comment 만 수정하려고 할 때, choice 필드가 필요하다고 한다.
# 단, choice 필드 또한 수정이 가능해야 하며 comment 필드 단독으로 수정도 가능해야 한다.
@api_view(['GET', 'PUT', 'DELETE'])
def answer_detail_update_delete(request, choice_pk, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if request.method == 'PUT':
        serializer = AnswerUpdateSerializer(answer, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        answer.delete()
        return Response({'answer': f'{answer_pk} deleted'}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)