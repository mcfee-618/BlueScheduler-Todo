from BlueScheduler.util.resolver import Resolver


def get_deley_tasks():
    plan_resolver = Resolver()
    plan_projects = plan_resolver.resolve("/mnt/e/projects/python/BlueScheduler/plans") 

    for plan_project_name in plan_projects:
        plan_project = plan_projects.get(plan_project_name)
        for plan_task in plan_project.get_tasks():
            if plan_task.is_delay():
                lo