import os
import statsd
import traceback
from github import Github

github_client = Github(os.getenv('GITHUB_TOKEN'))
statsd_client = statsd.StatsClient(os.getenv('STATSD_HOST'),os.getenv('STATSD_PORT'))

for repo in github_client.get_user().get_repos():
  try:
    latest_release = repo.get_latest_release()
    latest_release_published_date = latest_release.published_at
    commits_since_last_release = repo.get_commits(since=latest_release_published_date)
    statsd_client.gauge('github.' + repo.name + '.commits_since_last_release', commits_since_last_release.totalCount)
  except:
    print(traceback.format_exc())
    pass
