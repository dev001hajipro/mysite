import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        this return False for question whose pub_date is older than 1 day.
        """
        older_then_one_day = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=older_then_one_day)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        this return True for question whose pub_date is within the last day.
        """
        within_last_day = timezone.now() - datetime.timedelta(hours=23,
                                                              minutes=59, seconds=59)
        q = Question(pub_date=within_last_day)
        self.assertIs(q.was_published_recently(), True)


def create_question(text: str, days: float) -> None:
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        res = self.client.get(reverse('polls:index'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "No poll are available.")
        self.assertQuerysetEqual(res.context['latest_question_list'], [])

    def test_past_questions(self):
        q = create_question(text="Past question.", days=-30)
        res = self.client.get(reverse('polls:index'))
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(res.context['latest_question_list'], [q])

    def test_future_questions(self):
        q = create_question(text="Past question.", days=30)
        res = self.client.get(reverse('polls:index'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "No poll are available.")
        self.assertQuerysetEqual(res.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        q = create_question(text="Past question.", days=-30)
        create_question(text="Future question.", days=30)
        res = self.client.get(reverse('polls:index'))
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(res.context['latest_question_list'], [q])

    def test_2past_questions(self):
        q1 = create_question(text="Past question 1.", days=-30)
        q2 = create_question(text="Past question 2.", days=-5)
        res = self.client.get(reverse('polls:index'))
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(res.context['latest_question_list'], [q2, q1])
