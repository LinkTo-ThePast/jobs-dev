from dataclasses import dataclass;

@dataclass
class Job:
  job_id: str
  title: str
  state: str
  city: str
  job_type: str
  url: str
