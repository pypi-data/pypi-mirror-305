# cheutils

A set of basic reusable utilities and tools to facilitate quickly getting up and going on any machine learning project.

### Features

- model_options: methods such as get_regressor to get a handle on a configured estimator with a specified parameter dictionary or get_default_grid to get the configured hyperparameter grid
- model_builder: methods for building and executing ML pipeline steps e.g., fit, predict, score, params_optimization etc.
- project_tree: methods for accessing the project tree - e.g., get_data_dir() for accessing the configured data and get_output_dir() for the output folders, loading and savings Excel and CSV.
- common_utils: methods to support common programming tasks, such as labeling or tagging and date-stamping files
- propertiesutil: utility for managing properties files or project configuration, based on jproperties. The application configuration is expected to be available in a file named app-config.properties, which can be placed anywhere in the project root or any subfolder thereafter.
- decorator_debug, decorator_timer, and decorator_singleton: decorators for enabling logging and method timers; as well as a singleton decorator

### Usage
You import the `cheutils` module as per usual:
```
import cheutils
```
The following provide access to the properties file, usually expected to be named "app-config.properties" and typically found in the project data folder or anywhere either in the project root or any other subfolder
```
APP_PROPS = cheutils.AppProperties() # to load the app-config.properties file
```
Thereafter, you can read any properties using various methods such as:
```
DATA_DIR = APP_PROPS.get('project.data.dir')
```
You can also retrieve the path to the data folder, which is under the project root as follows:
```
cheutils.get_data_dir()  # returns the path to the project data folder, which is always interpreted relative to the project root
```
You can retrieve other properties as follows:
```
VALUES_LIST = APP_PROPS.get_list('some.configured.list') # e.g., some.configured.list=[1, 2, 3] or ['1', '2', '3']
VALUES_DIC = APP_PROPS.get_dic_properties('some.configured.dict') # e.g., some.configured.dict={'val1': 10, 'val2': 'value'}
BOL_VAL = APP_PROPS.get_bol('some.configured.bol') # e.g., some.configured.bol=True
```
You also have access to the LOGGER - you can simply call `LOGGER.debug()` in a similar way to you will when using loguru or standard logging 
calling `set_prefix()` on the LOGGER instance ensures the log messages are scoped to that context thereafter, 
which can be helpful when reviewing the generated log file (`app-log.log`) - the default prefix is "app-log".

You can get a handle to an application logger as follows:
```
LOGGER = cheutils.LoguruWrapper().get_logger()
```
You can set the logger prefix as follows:
```
LOGGER.set_prefix(prefix='my_project')
```
The `model_options` currently supports the following regressors: Lasso, LinearRegression, Ridge, GradientBoostingRegressor, XGBRegressor, LGBMRegressor, DecisionTreeRegressor, RandomForestRegressor
You can configure any of the models for your project with an entry in the app-config.properties as follows:
```
model.active.model_option=xgb_boost # with default parameters
```
You can get a handle to the corresponding regressor as follows:
```
regressor = cheutils.get_regressor(model_option='xgb_boost')
```
You can also configure the following property for example:
```
model.param_grids.xgb_boost={'learning_rate': {'type': float, 'start': 0.0, 'end': 1.0, 'num': 10}, 'subsample': {'type': float, 'start': 0.0, 'end': 1.0, 'num': 10}, 'min_child_weight': {'type': float, 'start': 0.1, 'end': 1.0, 'num': 10}, 'n_estimators': {'type': int, 'start': 10, 'end': 400, 'num': 10}, 'max_depth': {'type': int, 'start': 3, 'end': 17, 'num': 5}, 'colsample_bytree': {'type': float, 'start': 0.0, 'end': 1.0, 'num': 5}, 'gamma': {'type': float, 'start': 0.0, 'end': 1.0, 'num': 5}, 'reg_alpha': {'type': float, 'start': 0.0, 'end': 1.0, 'num': 5}, }
```
Thereafter, you can do the following:
```
regressor = cheutils.get_regressor(**get_params(model_option='xgb_boost'))
```
Thereafter, you can simply fit the model as follows:
```
cheutils.fit(regressor, X_train, y_train)
```
Given a default model parameter configuration (usually in the properties file), you can generate a promising parameter grid using RandomSearchCV as follows - i.e., the pipeline can either be an sklearn pipeline or an estimator:
```
cheutils.promising_params_grid(pipeline, X_train, y_train, grid_resolution=3, prefix='model_prefix')
```
You can run hyperparameter optimization or tuningas follows, if using hyperopt and Mlflow logging:
```
cheutils.params_optimization(pipeline, X_train, y_train, promising_params_grid=params_grid, with_narrower_grid=True, fine_search='hyperoptcv', prefix='model_prefix', mlflow_log=True)
```

