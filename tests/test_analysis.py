import unittest
from src.analysis import load_cases,summarize,total_hours

class TestProcessAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases=load_cases()
        cls.summary=summarize(cls.cases)
    def test_unique_cases(self):
        self.assertEqual(len(self.cases),1200)
        self.assertEqual(len({r["case_id"] for r in self.cases}),1200)
    def test_positive_times(self):
        self.assertTrue(all(total_hours(r,"as_is")>0 and total_hours(r,"to_be")>0 for r in self.cases))
    def test_route_counts(self):
        self.assertEqual(self.summary["all"]["cases"],self.summary["standard"]["cases"]+self.summary["exception"]["cases"])
    def test_nonnegative_savings(self):
        self.assertGreater(self.summary["all"]["handling_hours_saved"],0)
    def test_sla_range(self):
        for key in ("all","standard","exception"):
            for mode in ("as_is","to_be"):
                self.assertTrue(0<=self.summary[key][mode]["sla_48h_pct"]<=100)

if __name__=="__main__": unittest.main()
