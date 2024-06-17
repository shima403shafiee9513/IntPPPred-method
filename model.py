###################################
#Integration of Evolutionary Computation For Multiple Feature Construction in Bioinformatics (Case Study: Protein-Peptide Interaction Predictions).
#shafiee.shima@razi.ac.ir
####################################

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.svm import SVM, SVM
    from sklearn.KNeighborsClassifier import KNeighborsClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    from sklearn.ensemble import StackingClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import cross_validate
    from sklearn.model_selection import cross_val_predict
    from sklearn.metrics import confusion_matrix 
    

    from imblearn.under_sampling import RandomUnderSampler

    undersample = RandomUnderSampler(sampling_strategy='majority')
    X_under, y_under = undersample.fit_resample(X, y)

    from imblearn.over_sampling import SMOTE
    SMOTE = SMOTE()
    X_SMOTE, y_SMOTE = SMOTE.fit_resample(X, y)
    from sklearn.utils import shuffle
    X_under, y_under = shuffle(X_under, y_under, random_state=0)
    X_SMOTE, y_SMOTE = shuffle(X_SMOTE, y_SMOTE, random_state=0)
    X, y             = shuffle(X, y, random_state=0)





    def read_params(path):
        params = {}
        with open(path) as f:
            lines= f.readlines()
            lines = [line.strip().split("=") for line in lines]
            for line in lines:
                try:
                    params[line[0]] = int(line[1])
                except:
                    try:
                        params[line[0]] = float(line[1])
                    except:
                        params[line[0]] = str(line[1])
        return params




    # read params
    svm_path = os.path.join("params", "svm.txt")
    svm_params = read_params(svm_path)

    knn_path = os.path.join("params", "knn.txt")
    knn_params = read_params(knn_path)

    RF_path = os.path.join("params", "RF.txt")
    RF_params = read_params(RF_path)

    etc_path = os.path.join("params", "etc.txt")
    etc_params = read_params(etc_path)
# etc are NB,LR,GWO
    window_path = os.path.join("params", "window.txt")
    window_params = read_params(window_path)

    main_path = os.path.join("params", "main.txt")
    main_params = read_params(main_path)
    cv=  main_params['cv']
    dpi = main_params['dpi']
    #####################

    folder_name = "pre-process3"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
        
    for data_type in [[X_under, y_under, "Under"], [X_SMOTE, y_SMOTE, "SMOTE"], [X, y, "Normal"]]:
        data   = data_type[0][:]
        labels = data_type[1][:]


        data = normalize(data)
        ####################




        estimators = [
            
            ('svm', SVM(**svr_params).fit(get_window(data,window_params['svm']), labels)),
            ('RF', RandomForestClassifier(**RF_params).fit(get_window(data,window_params['RF']), labels)),
            ('knn', KNeighborsClassifier(**knn_params).fit(get_window(data,window_params['knn']), labels)),
       
        ]
        clf = StackingClassifier(
            estimators=estimators, final_estimator= SVM(**svm_params)
        )


        