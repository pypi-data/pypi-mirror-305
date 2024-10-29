"""Algorithms for logical alarms based on the axioms.

Formal verification of unsupervised evaluations is carried out by
using the agreements and disagreements between classifiers to detect
if they are misaligned given a safety specification.
"""

import itertools


class SingleClassifierAxiomAlarm:
    """Alarm based on the single classifier axioms for the ensemble members

    Initialize with 'classifiers_axioms', list of
    ntqr.r3.raxioms.SingleClassifierAxioms, one per classifier we want
    to compare.

    Also needs class that does SingleClassifierEvaluations given the
    axioms as 'cls_single_evals'
    """

    def __init__(self, Q, classifiers_axioms, cls_single_evals):
        """"""

        self.Q = Q

        self.classifiers_axioms = classifiers_axioms
        self.labels = classifiers_axioms[0].labels

        self.evals = [
            cls_single_evals(self.Q, axioms)
            for axioms in self.classifiers_axioms
        ]

    def set_safety_specification(self, factors):
        """Set alarm's safetySpecification given factors"""
        assert len(factors) == len(self.labels)
        self.safety_specification = LabelsSafetySpecification(factors)

    def misaligned_at_qs(self, qs, responses):
        """Boolean test to see if the classifiers violate the safety
        specification at given questions correct number."""

        assert self.check_responses(qs, responses)

        max_corrects = [
            sca_eval.max_correct_at_qs(qs, cresponses)
            for sca_eval, cresponses in zip(self.evals, responses)
        ]

        return any(
            (not self.safety_specification.is_satisfied(qs, max_correct))
            for max_correct in max_corrects
        )

    def misalignment_trace(self, responses):
        "Boolean trace of the classifiers test alignment."
        all_qs = self.evals[0].all_qs()
        trace = set(
            (qs, self.misaligned_at_qs(qs, responses)) for qs in all_qs
        )
        return trace

    def are_misaligned(self, responses):
        "Boolean test of misaligned"
        trace = self.misalignment_trace(responses)
        return all(list(zip(*trace))[1])

    def check_responses(self, qs, responses):
        "Checks logical constraints on responses."
        q = sum(qs)
        if q == self.Q:
            qs_check = True
        else:
            qs_check = False
        responses_check = all(
            [
                (q == sum(classifier_responses))
                for classifier_responses in responses
            ]
        )

        consistency_check = all([qs_check, responses_check])
        if consistency_check == False:
            print("q ", q, "Q ", self.Q),
            print("qs ", qs)
            print("responses ", responses)
            print("checks ", [qs_check, responses_check])

        return all([qs_check, responses_check])


class LabelsSafetySpecification:
    """Simple example of a safety specification.
    Parameters:
    ----------
    factors: list of factors to be used in safety
    specification tests, one per label.
    """

    def __init__(self, factors):

        self.factors = factors

    def is_satisfied(self, qs, correct_responses):
        """Checks that list of label accuracies satisfy the
        safety specification.

        Returns True if all labels satisfy the equation
          factor*correct_response - ql > 0
        given each label's factor and assumed number in
        the unknown test answer key, False otherwise."""
        tests = [
            (factor * correct_response - ql) > 0 if ql > 0 else True
            for factor, correct_response, ql in zip(
                self.factors, correct_responses, qs
            )
        ]
        return all(tests)

    def pair_safe_evaluations_at_qs(self, qs):
        """All pair evaluations satisfying safety spec at given qs."""
        correct_ranges = [
            [
                q_correct
                for q_correct in range(0, ql + 1)
                if ((factor * q_correct) - ql > 0)
            ]
            for factor, ql in zip(self.factors, qs)
        ]

        return [
            itertools.product(correct_range, repeat=2)
            for correct_range in correct_ranges
        ]


class GradeSafetySpecification:
    """Simple example of a safety specification.
    Parameters:
    ----------
    factors: list of factors to be used in safety
    specification tests, one per label.

    Returns:
    -------
    True if all labels satisfy factor_l*max_correct_l - ql > 0,
    False otherwise
    """

    def __init__(self, factors):

        self.factors = factors

    def is_satisfied(self, qs, correct_responses):
        """Checks that list of label accuracies satisfy the
        safety specification.

        Returns True if the max correct answers for labels satisfy
          factor*sum(correct_label) - Q > 0 given questions
          numbers 'qs',
          False otherwise.
        """
        Q = sum(qs)
        grade_test = self.factor * sum(correct_responses) - Q > 0
        return grade_test

    def pair_safe_evaluations_at_qs(self, qs):
        """All pair evaluations satisfying safety spec at given qs."""
        ql_ranges = (
            [q_correct for q_correct in range(0, ql + 1)] for ql in qs
        )
        pair_safe_evaluations = filter(
            lambda rs: self.is_satisfied(qs, rs), itertools.product(*ql_ranges)
        )
        return [
            itertools.product(correct_range, repeat=2)
            for correct_range in zip(*pair_safe_evaluations)
        ]
