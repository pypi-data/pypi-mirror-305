import typing
from typing import List
from typing import Tuple

from pypika import NULL
from pypika.functions import Cast
from pypika.terms import Field
from pypika.terms import Term
from pypika.terms import ValueWrapper

from tecton_core import data_types
from tecton_core.errors import TectonInternalError
from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper
from tecton_core.specs import RealtimeFeatureViewSpec
from tecton_core.specs.calculation_node_spec import AbstractSyntaxTreeNodeSpec
from tecton_core.specs.calculation_node_spec import LiteralValueNodeSpec


def build_calculation_sql_columns(
    feature_definition_namespaces: List[Tuple[FeatureDefinitionWrapper, str]], use_namespace_feature_prefix: bool
) -> List[Field]:
    calculation_projections = []
    for fdw, namespace in feature_definition_namespaces:
        sep = fdw.namespace_separator
        for calc in typing.cast(RealtimeFeatureViewSpec, fdw.fv_spec).calculation_features:
            output_column = f"{namespace}{sep}{calc.name}" if use_namespace_feature_prefix else calc.name
            calculation_sql = build_ast_node_sql(calc.root).as_(output_column)
            calculation_projections.append(calculation_sql)
    return calculation_projections


def build_ast_node_sql(ast_node: AbstractSyntaxTreeNodeSpec) -> Term:
    """Returns the pypika sql column expression for a single calculation feature."""
    if isinstance(ast_node, LiteralValueNodeSpec):
        return _build_literal_value_sql(ast_node)
    else:
        msg = f"In Calculation sql generation, AST node type {type(ast_node)} not supported."
        raise TectonInternalError(msg)


def _build_literal_value_sql(ast_node: LiteralValueNodeSpec) -> Term:
    if ast_node.dtype is None or ast_node.value is None:
        return NULL
    col = ValueWrapper(ast_node.value)
    if isinstance(ast_node.dtype, data_types.Int64Type):
        col = Cast(col, "BIGINT")
    elif isinstance(ast_node.dtype, data_types.Float64Type):
        col = Cast(col, "DOUBLE")
    return col
