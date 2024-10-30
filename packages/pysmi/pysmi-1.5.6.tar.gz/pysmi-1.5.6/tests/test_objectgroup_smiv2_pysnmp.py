#
# This file is part of pysmi software.
#
# Copyright (c) 2015-2020, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/pysmi/license.html
#
import sys

try:
    import unittest2 as unittest

except ImportError:
    import unittest

from pysmi.parser.smi import parserFactory
from pysmi.parser.dialect import smi_v2
from pysmi.codegen.pysnmp import PySnmpCodeGen
from pysmi.codegen.symtable import SymtableCodeGen
from pysnmp.smi.builder import MibBuilder


class ObjectGroupTestCase(unittest.TestCase):
    """
    TEST-MIB DEFINITIONS ::= BEGIN
    IMPORTS
      OBJECT-GROUP
        FROM SNMPv2-CONF;

    testObjectGroup OBJECT-GROUP
        OBJECTS         {
                            testStorageType,
                            testRowStatus
                        }
        STATUS          current
        DESCRIPTION
            "A collection of test objects."
     ::= { 1 3 }

    END
    """

    def setUp(self):
        ast = parserFactory(**smi_v2)().parse(self.__class__.__doc__)[0]
        mibInfo, symtable = SymtableCodeGen().gen_code(ast, {}, genTexts=True)
        self.mibInfo, pycode = PySnmpCodeGen().gen_code(
            ast, {mibInfo.name: symtable}, genTexts=True
        )
        codeobj = compile(pycode, "test", "exec")

        mibBuilder = MibBuilder()
        mibBuilder.loadTexts = True

        self.ctx = {"mibBuilder": mibBuilder}

        exec(codeobj, self.ctx, self.ctx)

    def testObjectGroupSymbol(self):
        self.assertTrue("testObjectGroup" in self.ctx, "symbol not present")

    def testObjectGroupName(self):
        self.assertEqual(self.ctx["testObjectGroup"].getName(), (1, 3), "bad name")

    def testObjectGroupDescription(self):
        self.assertEqual(
            self.ctx["testObjectGroup"].getDescription(),
            "A collection of test objects.",
            "bad DESCRIPTION",
        )

    def testObjectGroupObjects(self):
        self.assertEqual(
            self.ctx["testObjectGroup"].getObjects(),
            (("TEST-MIB", "testStorageType"), ("TEST-MIB", "testRowStatus")),
            "bad OBJECTS",
        )

    def testObjectGroupClass(self):
        self.assertEqual(
            self.ctx["testObjectGroup"].__class__.__name__,
            "ObjectGroup",
            "bad SYNTAX class",
        )


class ObjectGroupHyphenTestCase(unittest.TestCase):
    """
    TEST-MIB DEFINITIONS ::= BEGIN
    IMPORTS
      OBJECT-GROUP
        FROM SNMPv2-CONF;

    test-object-group OBJECT-GROUP
        OBJECTS         {
                            testStorageType,
                            testRowStatus
                        }
        STATUS          current
        DESCRIPTION
            "A collection of test objects."
     ::= { 1 3 }

    END
    """

    def setUp(self):
        ast = parserFactory(**smi_v2)().parse(self.__class__.__doc__)[0]
        mibInfo, symtable = SymtableCodeGen().gen_code(ast, {})
        self.mibInfo, pycode = PySnmpCodeGen().gen_code(ast, {mibInfo.name: symtable})
        codeobj = compile(pycode, "test", "exec")

        self.ctx = {"mibBuilder": MibBuilder()}

        exec(codeobj, self.ctx, self.ctx)

    def testObjectGroupSymbol(self):
        self.assertTrue("test_object_group" in self.ctx, "symbol not present")

    def testObjectGroupLabel(self):
        self.assertEqual(
            self.ctx["test_object_group"].getLabel(), "test-object-group", "bad label"
        )


suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite)
