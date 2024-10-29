"""
Evaluate noisy decision makers using logic and algebra.

Classes:

Functions:

Misc variables:

    __version__
    uci_adult_test_example
"""

__version__ = "0.4.1"

from ntqr.r2.examples import uciadult_label_counts

from ntqr.r2.datasketches import TrioLabelVoteCounts, TrioVoteCounts

from ntqr.r2.evaluators import (
    SupervisedEvaluation,
    ErrorIndependentEvaluation,
    MajorityVotingEvaluation,
)

import ntqr.statistics
import ntqr.r2
import ntqr.r3
