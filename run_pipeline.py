from run_pipeline.DataCleaningpipeline import DatacleanPipeline
from run_pipeline.feature_pipeline import RunFeaturePipeline

clean = DatacleanPipeline()
clean.RunningMethods()

feature = RunFeaturePipeline()
feature.RunMethods()


