import os
import tempfile
import unittest

from entry import EntryLogic


class EntryLogicEditTests(unittest.TestCase):
    def test_edit_updates_existing_entry_and_preserves_id(self):
        logic = EntryLogic([])
        original = logic.add("Salary", "2024-01-01", "Income", "Monthly pay", 1000)

        updated = logic.update(original.id, "Bonus", "2024-01-02", "Income", "Extra pay", 1500)

        self.assertEqual(updated.id, original.id)
        self.assertEqual(len(logic.entries), 1)
        self.assertEqual(logic.entries[0].title, "Bonus")
        self.assertEqual(logic.entries[0].amount, 1500)
        self.assertEqual(logic.entries[0].date, "2024-01-02")

    def test_save_and_load_persist_entries_to_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "entries.json")
            logic = EntryLogic([])
            logic.add("Salary", "2024-01-01", "Income", "Monthly pay", 1000)
            logic.save_to_file(file_path)

            reloaded = EntryLogic.from_file(file_path)

            self.assertEqual(len(reloaded.entries), 1)
            self.assertEqual(reloaded.entries[0].title, "Salary")
            self.assertEqual(reloaded.entries[0].amount, 1000)

    def test_from_file_returns_empty_logic_for_empty_json_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "empty.json")
            with open(file_path, "w", encoding="utf-8") as handle:
                handle.write("")

            reloaded = EntryLogic.from_file(file_path)

            self.assertEqual(reloaded.entries, [])


if __name__ == "__main__":
    unittest.main()
