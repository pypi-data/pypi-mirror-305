from sklearn.metrics import mean_absolute_error


def mae(app_gt, app_pred):
    return mean_absolute_error(app_gt, app_pred)
