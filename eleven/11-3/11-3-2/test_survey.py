import pytest
from survey import AnonymousSurvey

@pytest.fixture

def language_survey():
    """提一个可供所有测试函数使用的AnonymousSurvey实例"""
    question="what language did you first learn to speak? "
    language_survey=AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """测试单个答案会被存储"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    """测试3个答案会被存储"""
    responses=('English','Spanish','Mandarin')
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses

