import os
import numpy as np
from collections import Counter
from concurrent.futures import as_completed, ProcessPoolExecutor
from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, root_mean_squared_error
from logging import basicConfig, INFO, getLogger

logger = getLogger(__name__)
basicConfig(level=INFO, format='[%(asctime)s %(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def train_evaluate(model, X_train, X_test, y_train, y_test, describe='准确率', verbose=True, return_predict=False,
                   evaluate_func=accuracy_score):
	"""Train and evaluate a model

	Parameters
    ----------
	model: Model
	X_train:
	X_test:
	y_train:
	y_test:
	verbose:
	describe:
	return_predict: whether return predictions
	evaluate_func: accuracy_score, mean_squared_error, root_mean_squared_error etc.

	Returns
    -------
    score or (score, predictions)

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearntools import train_evaluate
    >>> X, y = np.arange(20).reshape((10, 2)), range(10)
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    >>> model = RandomForestClassifier(n_estimators=837, bootstrap=False)
    >>> train_evaluate(model, X_train, X_test, y_train, y_test)
    0.88
	"""
	
	model.fit(X_train, y_train)
	prediction = model.predict(X_test)
	if 'classifier' == model._estimator_type:
		evaluate_func = accuracy_score
	else:
		evaluate_func = evaluate_func or mean_squared_error
	score = evaluate_func(y_test, prediction)
	if verbose:
		if evaluate_func == accuracy_score:
			logger.info(f'{describe}: {score:.1%}')
		else:
			if '准确率' == describe:
				if evaluate_func == mean_squared_error:
					describe = 'MSE'
				elif evaluate_func == root_mean_squared_error:
					describe = 'RMSE'
			logger.info(f'{describe}: {score:.2f}')
	if return_predict:
		return score, prediction
	return score


def train_evaluate_split(model, X, y, test_size=0.2, describe='准确率', verbose=True, return_predict=False,
                         random_state=42, evaluate_func=accuracy_score):
	"""Train and evaluate a model

	Parameters
	----------
	model: Model
	X:
	y:
	test_size:
	verbose:
	describe:
	return_predict: whether return predictions
	random_state:
	evaluate_func: accuracy_score, mean_squared_error, root_mean_squared_error etc.

	Returns
	-------
	score or (score, predictions)

	Examples
	--------
	>>> import numpy as np
	>>> from sklearn.ensemble import RandomForestClassifier
	>>> from sklearntools import train_evaluate_split
	>>> X, y = np.arange(20).reshape((10, 2)), range(10)
	>>> model = RandomForestClassifier(n_estimators=837, bootstrap=False)
	>>> train_evaluate_split(model, X, y, test_size=0.2)
	0.88
	"""
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
	return train_evaluate(model, X_train, X_test, y_train, y_test, describe, verbose, return_predict, evaluate_func)


def search_model_params(model_name, X_train, X_test, y_train, y_test, param_grid, result_num=5, iter_num=8,
                        n_proc: int = None):
	"""
	Train and evaluate a model

	Parameters
	----------
	model_name:
	X_train:
	X_test:
	y_train:
	y_test:
	param_grid:
	result_num:
	iter_num:
	n_proc：进程数

	Examples
	--------
	>>> import numpy as np
	>>> from sklearn.ensemble import RandomForestClassifier
	>>> from sklearn.model_selection import train_test_split
	>>> from sklearntools import search_model_params
	>>> X, y = np.arange(20).reshape((10, 2)), range(10)
	>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
	>>> param_grid = {'n_estimators': np.arange(800, 820, 1), 'bootstrap': [False, True]}
	>>> search_model_params(RandomForestClassifier, X_train, X_test, y_train, y_test, param_grid, result_num=3)
	[{'bootstrap': False, 'n_estimators': 565}]
	"""
	classifier = 'classifier' == model_name._estimator_type
	n_proc = n_proc or os.cpu_count()
	with ProcessPoolExecutor(n_proc) as executor:
		results = [executor.submit(_search_params, model_name, classifier, X_train, X_test, y_train, y_test, params) for
		           params in ParameterGrid(param_grid)]
		results = [r.result() for r in as_completed(results)]
	results.sort(key=lambda x: x[1], reverse=False)
	params = []
	for param, score in results[:result_num]:
		params.append(param)
		if classifier:
			logger.info(f'param: {param}\tscore: {score:.1%}')
		else:
			logger.info(f'param: {param}\tscore: {score:.4f}')
		_evaluate_params(model_name, classifier, X_train, X_test, y_train, y_test, param, iter_num)
	return params


def search_model_params_split(model_name, X, y, param_grid, test_size=0.2, result_num=5, iter_num=8, random_state=42,
                              n_proc: int = None):
	"""Train and evaluate a model

	Parameters
	----------
	model_name:
	X:
	y:
	test_size:
	param_grid:
	result_num:
	iter_num:
	random_state:
	n_proc：进程数

	Examples
	--------
	>>> import numpy as np
	>>> from sklearn.ensemble import RandomForestClassifier
	>>> from sklearntools import search_model_params_split
	>>> X, y = np.arange(20).reshape((10, 2)), range(10)
	>>> param_grid = {'n_estimators': np.arange(800, 820, 1), 'bootstrap': [False, True]}
	>>> search_model_params_split(RandomForestClassifier, X, y, param_grid, test_size=0.2, result_num=3)
	[{'bootstrap': False, 'n_estimators': 565}]
	"""
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
	return search_model_params(model_name, X_train, X_test, y_train, y_test, param_grid, result_num, iter_num, n_proc)


def search_test_size(model, X, y, test_sizes=np.arange(0.15, 0.36, 0.01), random_state=42, evaluate_func=None,
                     n_proc: int = None, topK=5):
	"""
	Examples
	--------
	>>> from sklearntools import search_test_size
	>>> search_test_size(model, X, y, random_state=42, evaluate_func=accuracy_score)
	0.2
	"""
	classifier = 'classifier' == model._estimator_type
	n_proc = n_proc or os.cpu_count()
	with ProcessPoolExecutor(n_proc) as executor:
		results = [executor.submit(_search_test_size, model, X, y, test_size, random_state, evaluate_func) for
		           test_size in test_sizes]
		results = [r.result() for r in as_completed(results)]
	results.sort(key=lambda x: x[1], reverse=True)
	if classifier:
		for test_size, score in results[:topK]:
			logger.info(f'test_size: {test_size:.0%} \t score: {score:.2%}')
	else:
		for test_size, score in results[:topK]:
			logger.info(f'test_size: {test_size:.0%} \t score: {score}:4f')
	return results[0][0]


def search_random_state(model, X, y, random_states=np.arange(0, 20, 1), test_size=0.2, evaluate_func=None,
                        n_proc: int = None, topK=5):
	"""
	Examples
	--------
	>>> from sklearntools import search_random_state
	>>> search_random_state(model, X, y, test_size=0.2, evaluate_func=accuracy_score)
	42
	"""
	classifier = 'classifier' == model._estimator_type
	n_proc = n_proc or os.cpu_count()
	with ProcessPoolExecutor(n_proc) as executor:
		results = [executor.submit(_search_random_state, model, X, y, test_size, random_state, evaluate_func) for
		           random_state in random_states]
		results = [r.result() for r in as_completed(results)]
	results.sort(key=lambda x: x[1], reverse=True)
	if classifier:
		for random_state, score in results[:topK]:
			logger.info(f'random_state: {random_state} \t score: {score:.2%}')
	else:
		for random_state, score in results[:topK]:
			logger.info(f'random_state: {random_state} \t score: {score}:4f')
	return results[0][0]


def _search_test_size(model, X, y, test_size, random_state, evaluate_func):
	return test_size, train_evaluate_split(model, X, y, test_size, None, False, False, random_state, evaluate_func)


def _search_random_state(model, X, y, test_size, random_state, evaluate_func):
	return random_state, train_evaluate_split(model, X, y, test_size, None, False, False, random_state, evaluate_func)


def _search_params(model_name, classifier, X_train, X_test, y_train, y_test, params):
	model = model_name(**params)
	model.fit(X_train, y_train)
	score = model.score(X_test, y_test)
	if not classifier:
		score = round(score, 4)
	return params, score


def _evaluate_params(model_name, classifier, X_train, X_test, y_train, y_test, param, iter_num, n_proc: int = None):
	n_proc = n_proc or os.cpu_count()
	with ProcessPoolExecutor(n_proc) as executor:
		results = [executor.submit(
			_search_params, model_name, classifier, X_train, X_test, y_train, y_test, param) for _ in range(iter_num)
		]
		results = [r.result() for r in as_completed(results)]
	results = [result[1] for result in results]
	mean_score = sum(results) / len(results)
	counter = Counter(results)
	results = sorted(counter.items(), key=lambda x: x[0], reverse=True)
	if classifier:
		for score, count in results:
			logger.info(f'\tscore: {score:.1%}\tcount: {count}')
		logger.info(f'平均准确率: {mean_score:.1%}')
	else:
		for score, count in results:
			logger.info(f'\tscore: {score:.4f}\tcount: {count}')
		logger.info(f'平均分数: {mean_score:.4f}')


def multi_round_evaluate(X: np.ndarray, y: np.ndarray, *models, **kwargs):
	""" 对比多个模型的稳定评分

	Parameters
	----------
	X:
	y:

	Examples
	--------
	>>> from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
	>>> from sklearntools import multi_round_evaluate
	>>> multi_round_evaluate(df.values, y, RandomForestClassifier(), GradientBoostingClassifier(), num_rounds=10, test_size=0.2)
	"""
	assert len(models) >= 1, 'models must be'
	num_rounds = kwargs.pop('num_rounds') if 'num_rounds' in kwargs else 100
	test_size = kwargs.pop('test_size') if 'test_size' in kwargs else 0.2
	n_proc = kwargs.pop('n_proc') if 'n_proc' in kwargs else os.cpu_count()
	with ProcessPoolExecutor(n_proc) as executor:
		results = [executor.submit(one_round_evaluate, X, y, test_size, *models) for _ in range(num_rounds)]
		results = [r.result() for r in as_completed(results)]
	results = np.array(results)
	return results.mean(axis=0)


def one_round_evaluate(X: np.ndarray, y: np.ndarray, test_size: float, *models):
	scores = []
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=11)
	for i, model in enumerate(models):
		model.fit(X_train, y_train)
		scores.append(model.score(X_test, y_test))
	return scores
