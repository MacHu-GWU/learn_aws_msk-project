# -*- coding: utf-8 -*-

import cottonformation as cft
from cottonformation.res import msk

template = cft.Template(
    Description="AWS Kafka Cluster",
)

param_project_name = cft.Parameter(
    "ProjectName",
    Type=cft.Parameter.TypeEnum.String,
)

param_env_name = cft.Parameter(
    "ProjectName",
    Type=cft.Parameter.TypeEnum.String,
)

msk.Cluster(
    "MSKCluster",
)