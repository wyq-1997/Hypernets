from hypernets.conf import configure, Configurable, Int, String, Bool, Float, Enum


@configure()
class TabularCfg(Configurable):
    joblib_njobs = \
        Int(-1, allow_none=True,
            help='"n_jobs" setting for joblib task.'
            ).tag(config=True)

    multi_collinearity_sample_limit = \
        Int(10000, min=100,
            help='maximum number to run multi collinearity.'
            ).tag(config=True)

    permutation_importance_sample_limit = \
        Int(10000, min=100,
            help='maximum number to run permutation importance.'
            ).tag(config=True)

    cache_strategy = \
        Enum(['data', 'transform', 'disabled'],
             default_value='transform',
             config=True,
             help='dispatcher backend',
             )

    cache_dir = \
        String('cache_dir',
               allow_none=False,
               config=True,
               help='the directory to store cached data, read/write permissions are required.')

    geohash_precision = \
        Int(12, min=2,
            config=True,
            help=''
            )

    auto_categorize = \
        Bool(True,
             config=True,
             help=''
             )

    auto_categorize_shape_exponent = \
        Float(0.5,
              config=True,
              help=''
              )

    column_selector_text_word_count_threshold = \
        Int(10, min=1,
            config=True,
            help=''
            )

    tfidf_max_feature_count = \
        Int(1000, min=2,
            config=True,
            help=''
            )

    tfidf_primitive_output_feature_count = \
        Int(30, min=2,
            config=True,
            help=''
            )
