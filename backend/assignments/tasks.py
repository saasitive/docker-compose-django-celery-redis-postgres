from celery import shared_task

from assignments.models import Assignment


@shared_task(bind=True)
def task_execute(self, job_params):

    assignment = Assignment.objects.get(pk=job_params["db_id"])

    assignment.sum = assignment.first_term + assignment.second_term

    assignment.save()
