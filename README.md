
# ML.NET Aegirsoft

[ML.NET](https://www.microsoft.com/net/learn/apps/machine-learning-and-ai/ml-dotnet) is a cross-platform open-source machine learning framework that makes machine learning accessible to .NET developers.


# Automate ML.NET models generation (Preview state)

The previous samples show you how to use the ML.NET API 1.0 (GA since May 2019).

However, we're also working on simplifying ML.NET usage with additional technologies that automate the creation of the model for you so you don't need to write the code by yourself to train a model, you simply need to provide your datasets. The "best" model and the code for running it will be generated for you.

These additional technologies for automating model generation are in PREVIEW state and currently only support *Binary-Classification, Multiclass Classification and Regression*. In upcoming versions we'll be supporting additional ML Tasks such as *Recommendations, Anomaly Detection, Clustering, etc.*.

## CLI samples: (Preview state)

The ML.NET CLI (command-line interface) is a tool you can run on any command-prompt (Windows, Mac or Linux) for generating good quality ML.NET models based on training datasets you provide. In addition, it also generates sample C# code to run/score that model plus the C# code that was used to create/train it so you can research what algorithm and settings it is using.

| CLI (Command Line Interface) samples |
|----------------------------------|
| [Binary Classification sample](/samples/CLI/BinaryClassification_CLI) |
| [MultiClass Classification sample](/samples/CLI/MulticlassClassification_CLI) |
| [Regression sample](/samples/CLI/Regression_CLI) |


## AutoML API samples: (Preview state)

**THESE SAMPLES USE THE 0.1.x VERSION OF THE AUTOML API. WHILE THESE APIS STILL WORK IN VERSION 0.2.x WE RECOMMEND USING THE NEW APIS INTRODUCED IN 0.2.x AND LATER. FOR 0.2.x SAMPLES, SEE [ML.NET 2.0 Samples](samples/csharp/getting-started/MLNET2/README.md)**. 

ML.NET AutoML API is basically a set of libraries packaged as a NuGet package you can use from your .NET code. AutoML eliminates the task of selecting different algorithms, hyperparameters. AutoML will intelligently generate many combinations of algorithms and hyperparameters and will find high quality models for you.

| AutoML API samples                    |
|----------------------------------|
| [Binary Classification sample](/samples/csharp/getting-started/BinaryClassification_AutoML) |
| [MultiClass Classification sample](/samples/csharp/getting-started/MulticlassClassification_AutoML) |
| [Ranking sample](/samples/csharp/getting-started/Ranking_AutoML/Ranking) |
| [Regression sample](/samples/csharp/getting-started/Regression_AutoML) |
| [Advanced experiment sample](/samples/csharp/getting-started/AdvancedExperiment_AutoML) |


-------------------------------------------------------
## Translations of Samples:
- [Chinese Simplified](https://github.com/feiyun0112/machinelearning-samples.zh-cn)

# Learn more

See [ML.NET Guide](https://docs.microsoft.com/en-us/dotnet/machine-learning/) for detailed information on tutorials, ML basics, etc.

# API reference

Check out the [ML.NET API Reference](https://docs.microsoft.com/dotnet/api/?view=ml-dotnet) to see the breadth of APIs available.


