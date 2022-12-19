
# ML.NET Aegirsoft

[ML.NET](https://www.microsoft.com/net/learn/apps/machine-learning-and-ai/ml-dotnet) is a cross-platform open-source machine learning framework that makes machine learning accessible to .NET developers.

In this GitHub repo, we provide samples which will help you get started with ML.NET and how to infuse ML into existing and new .NET apps.

**Note:** Please open issues related to [ML.NET](https://www.microsoft.com/net/learn/apps/machine-learning-and-ai/ml-dotnet) framework in the [Machine Learning repository](https://github.com/dotnet/machinelearning/issues). Please create the issue in this repo only if you face issues with the samples in this repository.

There are two types of samples/apps in the repo:

* Getting Started  ![](./images/app-type-getting-started-term-cursor.png) : ML.NET code focused samples for each ML task or area, usually implemented as simple console apps.

* End-End apps ![](./images/app-type-e2e-black.png) : End-user sample web and desktop apps infused with Machine Learning models based on ML.NET.

The official ML.NET samples are divided in multiple categories depending on the scenario and machine learning problem/task, accessible through the following tables:



<br>
<br>

<table >
  <tr>
    <td align="middle" colspan="3">Cross Cutting Scenarios</td>
  </tr>
  <tr>
  <td align="middle"><img src="images/web.png" alt="web image" ><br><img src="images/app-type-e2e-black.png" alt="End-to-end app icon"><br><b>Scalable Model on WebAPI<br><a href="samples/csharp/end-to-end-apps/ScalableMLModelOnWebAPI-IntegrationPkg">C#</a><b></td>
  <td align="middle"><img src="images/web.png" alt="web image" ><br><img src="images/app-type-e2e-black.png" alt="End-to-end app icon"><br><b>Scalable Model on Razor web app<br><a href="samples/modelbuilder/BinaryClassification_Sentiment_Razor">C#</a><b></td>
  <td align="middle"><img src="images/azure-functions-20.png" alt="Azure functions logo"><br><img src="images/app-type-e2e-black.png" alt="End-to-end app icon"><br><b>Scalable Model on Azure Functions<br><a href="samples/csharp/end-to-end-apps/ScalableMLModelOnAzureFunction">C#</a><b></td>
</tr>
<tr>
  <td align="middle"><img src="images/smile.png" alt="Database chart"><br><img src="images/app-type-e2e-black.png" alt="End-to-end app icon"><br><b>Scalable Model on Blazor web app<br><a href="samples/csharp/end-to-end-apps/ScalableSentimentAnalysisBlazorWebApp">C#</a><b></td>
  <td align="middle"><img src="images/large-data-set.png" alt="large file chart"><br><img src="images/app-type-getting-started-term-cursor.png" alt="Getting started icon"><br><b>Large Datasets<br><a href="samples/csharp/getting-started/LargeDatasets">C#</a><b></td>
  <td align="middle"><img src="images/database.png" alt="Database chart"><br><img src="images/app-type-getting-started-term-cursor.png" alt="Getting started icon"><br><b>Loading data with DatabaseLoader<br><a href="samples/csharp/getting-started/DatabaseLoader">C#</a><b></td>
  </tr>
  <tr>
  <td align="middle"><img src="images/database.png" alt="Database chart"><br><img src="images/app-type-getting-started-term-cursor.png" alt="Getting started icon"><br><b>Loading data with  LoadFromEnumerable<br><a href="samples/csharp/getting-started/DatabaseIntegration">C#</a><b></td>
  <td align="middle"><img src="images/model-explain-smaller.png" alt="Model explainability chart"><br><img src="images/app-type-e2e-black.png" alt="End-to-end app icon"><br><b>Model Explainability<br><a href="samples/csharp/end-to-end-apps/Model-Explainability">C#</a></b></td>
  <td align="middle"><img src="images/extensibility.png" alt="Extensibility icon"><br><img src="images/app-type-e2e-black.png" alt="End-to-end app icon"><br><b>Export to ONNX<br><a href="samples/csharp/getting-started/Regression_ONNXExport">C#</a></b></td>
  </tr>
</table>


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


