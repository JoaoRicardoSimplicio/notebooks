import django_rq

from datetime import datetime

from django_rq.management.commands import rqscheduler

from notebook.tarefas.atualiza import atualiza_notebooks


scheduler = django_rq.get_scheduler()


def remove_atualizacoes_anteriores() -> None:
    for job in scheduler.get_jobs():
        job.delete()


def agenda_atualizacao() -> None:
    scheduler.schedule(
        scheduled_time=datetime.utcnow(),
        func=atualiza_notebooks,
        interval=60
    )


class Command(rqscheduler.Command):

    def handle(self, *args, **kwargs) -> None:
        remove_atualizacoes_anteriores()
        agenda_atualizacao()
        super(Command, self).handle(*args, **kwargs)
