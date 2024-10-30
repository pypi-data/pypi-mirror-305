from cubicweb.devtools.testlib import CubicWebTC
from cubicweb import Unauthorized


class PeriodicallyResetCounterTC(CubicWebTC):
    def setup_database(self):
        with self.admin_access.cnx() as cnx:
            self.counter = cnx.create_entity("PeriodicallyResetCounter")
            cnx.commit()

    def test(self):
        with self.admin_access.cnx() as cnx:
            c_eid = self.counter.eid
            counter = cnx.find("PeriodicallyResetCounter", eid=c_eid).one()
            self.assertEqual(counter.initial_value, 0)
            self.assertEqual(counter.increment, 1)
            self.assertEqual(counter.reset_every, "year")
            entity = cnx.entity_from_eid(self.counter.eid)
            self.assertEqual(entity.next_value(), 1)
            self.assertEqual(entity.next_value(), 2)
            cnx.rollback()
            self.assertEqual(entity.next_value(), 1)

    def test_admin_create_counter_value(self):
        """
        Trying: admin try to create a PeriodicallyResetCounter with a particular value
        Expecting: a PeriodicallyResetCounter is created
        """
        with self.admin_access.cnx() as cnx:
            self.counter = cnx.create_entity("PeriodicallyResetCounter", value=10)
            cnx.commit()

    def test_admin_update_counter_value_ko(self):
        """
        Trying: admin try to update a PeriodicallyResetCounter value
        Expecting: Unauthorized error is raised
        """
        with self.admin_access.cnx() as cnx:
            c_eid = self.counter.eid
            counter = cnx.find("PeriodicallyResetCounter", eid=c_eid).one()
            print(counter.value)
            with self.assertRaises(Unauthorized):
                counter.cw_set(value=1)
                cnx.commit()


if __name__ == "__main__":
    from logilab.common.testlib import unittest_main

    unittest_main()
