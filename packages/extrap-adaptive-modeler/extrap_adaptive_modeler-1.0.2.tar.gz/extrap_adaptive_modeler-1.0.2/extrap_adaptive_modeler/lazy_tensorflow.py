# This file is part of the Extra-P Adaptive Modeler software (https://github.com/extra-p/extrap-adaptive-modeler)
#
# Copyright (c) 2024, Technical University of Darmstadt, Germany
#
# This software may be modified and distributed under the terms of a BSD-style license.
# See the LICENSE file in the base directory for details.

import logging
import os


def load_tensorflow():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"
    os.environ['TF_USE_LEGACY_KERAS'] = "1"

    import tensorflow as tf
    physical_devices = tf.config.experimental.list_physical_devices('GPU')

    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
    except Exception as e:
        logging.info("GPU could not be configured.")

    return tf
