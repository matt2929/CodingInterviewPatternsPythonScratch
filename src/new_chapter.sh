#!/bin/zsh

chapter_name="$1"
echo "Creating a new chapter ${chapter_name}"
export lower_case_name=`echo "$chapter_name" | tr '[:upper:]' '[:lower:]'`
export upper_case_name=`echo "$chapter_name" | tr '[:lower:]' '[:upper:]'`
echo
mkdir "${lower_case_name}"
cd "${lower_case_name}"
touch __init__.py
touch "${lower_case_name}.py"
echo "class ${upper_case_name}:" >> "${lower_case_name}.py"
echo "    ..." >> "${lower_case_name}.py"
cd ../..
cd tests
mkdir "${lower_case_name}_tests"
cd "${lower_case_name}_tests"
touch __init__.py
touch "${lower_case_name}_tests.py"
echo "import unittest" >> "${lower_case_name}_tests.py"
echo "from parameterized import parameterized" >> "${lower_case_name}_tests.py"
echo "from ${lower_case_name}.${lower_case_name} import ${upper_case_name}" >> "${lower_case_name}_tests.py"
echo "" >> "${lower_case_name}_tests.py"
echo "class ${upper_case_name}Tests(unittest.TestCase):" >> "${lower_case_name}_tests.py"

echo "" >> "${lower_case_name}_tests.py"
echo "
  @parameterized.expand([
        ('a', False),
        ('b', False),
    ])
  def test_${lower_case_name}(self, input, expected):
      ${lower_case_name} = ${upper_case_name}()" >> "${lower_case_name}_tests.py"