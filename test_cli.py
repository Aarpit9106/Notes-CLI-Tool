import subprocess
import re
import sys
import os

def run_cmd(cmd, expect_error_msg=False):
    print(f"\n[TEST] Running: {' '.join(cmd)}")
    # Run command and capture output
    # By forcing PYTHONIOENCODING=utf-8, we ensure rich characters don't break Windows console handling in subprocess
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    output = (result.stdout or '') + (result.stderr or '')
    
    if expect_error_msg:
        if "Error:" in output or result.returncode != 0:
            print("✅ PASSED (Expected error encountered)")
            return True, output
        else:
            print("❌ FAILED: Expected an error but got none.")
            return False, output
    else:
        if "Error:" in output or result.returncode != 0:
            print(f"❌ FAILED: Command threw an error or exit code {result.returncode}")
            print(f"Output:\n{output.strip()}")
            return False, output
        else:
            print("✅ PASSED")
            return True, output

def extract_id(output):
    # Looking for "Note added with ID 5"
    match = re.search(r"ID (\d+)", output)
    if match:
        return match.group(1)
    return None

def main():
    print("=== Notes CLI Automated Test Suite ===")
    
    commands_to_test = [
        {"cmd": ["notes", "--help"]},
        {"cmd": ["notes", "list"]},
        {"cmd": ["notes", "dashboard"]},
        {"cmd": ["notes", "insights"]},
        {"cmd": ["notes", "replay", "week"]},
        {"cmd": ["notes", "send-future", "Automated future test", "--date", "2030-01-01"]},
        {"cmd": ["notes", "fakecommand"], "expect_error": True},
    ]
    
    passed = 0
    failed = 0
    
    # 1. Run basic read commands
    for test in commands_to_test:
        success, _ = run_cmd(test["cmd"], expect_error_msg=test.get("expect_error", False))
        if success: passed += 1
        else: failed += 1

    # 2. Run state-dependent workflows (Add -> View -> Edit -> Link -> Search -> Delete)
    # Add Note 1
    success, output = run_cmd(["notes", "add", "Test Note Alpha", "--tag", "autotag1", "--mood", "focused"])
    if not success:
        print("Fatal: Could not add note. Aborting dependent tests.")
        sys.exit(1)
    passed += 1
    
    id1 = extract_id(output)
    
    # Add Note 2
    success, output = run_cmd(["notes", "add", "Test Note Beta", "--tag", "autotag2", "--mood", "happy"])
    if not success:
        print("Fatal: Could not add note 2. Aborting dependent tests.")
        sys.exit(1)
    passed += 1
    
    id2 = extract_id(output)
    
    if not id1 or not id2:
        print("Fatal: Could not extract Note IDs from outputs. Check output formatting.")
        sys.exit(1)
        
    print(f"\n[INFO] Extracted IDs: Note 1 ({id1}), Note 2 ({id2})")
    
    # View Note 1
    success, _ = run_cmd(["notes", "view", id1])
    if success: passed += 1
    else: failed += 1
        
    # Edit Note 1
    success, _ = run_cmd(["notes", "edit", id1, "--tag", "updated_autotag", "--favorite"])
    if success: passed += 1
    else: failed += 1
        
    # Link Notes
    success, _ = run_cmd(["notes", "link", id1, id2])
    if success: passed += 1
    else: failed += 1
        
    # View Links
    success, _ = run_cmd(["notes", "links", id1])
    if success: passed += 1
    else: failed += 1
        
    # Search
    success, _ = run_cmd(["notes", "search", "Test Note Alpha"])
    if success: passed += 1
    else: failed += 1
        
    # Search Mood
    success, _ = run_cmd(["notes", "mood", "focused"])
    if success: passed += 1
    else: failed += 1
        
    # Delete Notes
    success, _ = run_cmd(["notes", "delete", id1])
    if success: passed += 1
    else: failed += 1
        
    success, _ = run_cmd(["notes", "delete", id2])
    if success: passed += 1
    else: failed += 1
        
    # Verify Deletion (Expected to fail/throw error)
    success, _ = run_cmd(["notes", "view", id1], expect_error_msg=True)
    if success: passed += 1
    else: failed += 1

    print("\n=== Test Suite Summary ===")
    print(f"Total Tests Run: {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed > 0:
        sys.exit(1)
    else:
        print("\n🎉 ALL TESTS PASSED! The CLI is production-ready.")
        sys.exit(0)

if __name__ == "__main__":
    main()
