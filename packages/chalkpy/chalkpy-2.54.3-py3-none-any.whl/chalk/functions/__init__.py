from __future__ import annotations

from typing import Any, Literal, Union

from chalk.features.underscore import (
    Underscore,
    UnderscoreBinaryOp,
    UnderscoreBytesToString,
    UnderscoreCoalesce,
    UnderscoreCosineSimilarity,
    UnderscoreFunction,
    UnderscoreGetJSONValue,
    UnderscoreGunzip,
    UnderscoreMD5,
    UnderscoreSagemakerPredict,
    UnderscoreStringToBytes,
    UnderscoreTotalSeconds,
)

########################################################################################################################
# String Functions                                                                                                     #
########################################################################################################################


def replace(expr: Underscore | Any, old: str, new: str):
    """Replace all occurrences of a substring in a string with another substring.

    Parameters
    ----------
    expr
        The string to replace the substring in.
    old
        The substring to replace.
    new
        The substring to replace the old substring with.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    normalized_name: str = F.replace(_.name, " ", "_")
    """
    return UnderscoreFunction("replace", expr, old, new)


def like(expr: Underscore | Any, pattern: str):
    """
    Evaluates if the string matches the pattern.

    Patterns can contain regular characters as well as wildcards.
    Wildcard characters can be escaped using the single character
    specified for the escape parameter. Matching is case-sensitive.

    Note: The wildcard `%` represents 0, 1 or multiple characters
    and the wildcard `_` represents exactly one character.

    For example, the pattern `John%` will match any string that starts
    with `John`, such as `John`, `JohnDoe`, `JohnSmith`, etc.

    The pattern `John_` will match any string that starts with `John`
    and is followed by exactly one character, such as `JohnD`, `JohnS`, etc.
    but not `John`, `JohnDoe`, `JohnSmith`, etc.

    Parameters
    ----------
    expr
        The string to check against the pattern.
    pattern
        The pattern to check the string against.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    is_john: bool = F.like(_.name, "John%")
    """
    return UnderscoreFunction("like", expr, pattern)


def regexp_like(expr: Underscore | Any, pattern: str):
    """
    Evaluates the regular expression pattern and determines if it is contained within string.

    This function is similar to the `like` function, except that the pattern only needs to be
    contained within string, rather than needing to match all the string.
    In other words, this performs a contains operation rather than a match operation.
    You can match the entire string by anchoring the pattern using `^` and `$`.

    Parameters
    ----------
    expr
        The string to check against the pattern.
    pattern
        The regular expression pattern to check the string against.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    is_john: bool = F.regexp_like(_.name, "^John.*$")
    """
    return UnderscoreFunction("regexp_like", expr, pattern)


def trim(expr: Underscore | Any):
    """
    Remove leading and trailing whitespace from a string.

    Parameters
    ----------
    expr
        The string to trim.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    trimmed_name: str = F.trim(_.name)
    """
    return UnderscoreFunction("trim", expr)


def starts_with(expr: Underscore | Any, prefix: Underscore | Any):
    """
    Evaluates if the string starts with the specified prefix.

    Parameters
    ----------
    expr
        The string to check against the prefix.
    prefix
        The prefix or feature to check if the string starts with.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    category: str
    ...    is_food: bool = F.starts_with(_.name, "Food")
    """
    return UnderscoreFunction("starts_with", expr, prefix)


def ends_with(expr: Underscore | Any, suffix: Underscore | Any):
    """
    Evaluates if the string ends with the specified suffix.

    Parameters
    ----------
    expr
        The string to check against the suffix.
    suffix
        The suffix or feature to check if the string ends with.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    category: str
    ...    is_food: bool = F.ends_with(_.name, "Food")
    """
    return UnderscoreFunction("ends_with", expr, suffix)


def substr(expr: Underscore, start: int, length: int | None = None):
    """
    Extract a substring from a string.

    Parameters
    ----------
    expr
        The string to extract the substring from.
    start
        The starting index of the substring (0-indexed).
    length
        The length of the substring. If None, the substring will extend to the end of the string.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    category: str
    ...    cat_first_three: str = F.substr(_.category, 0, 3)
    """
    if length is None:
        return UnderscoreFunction("substr", expr, start + 1)
    return UnderscoreFunction("substr", expr, start + 1, length)


def reverse(expr: Underscore | Any):
    """
    Reverse the order of a string.

    Parameters
    ----------
    expr
        The string to reverse.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    name: str
    ...    reversed_name: str = F.reverse(_.name)
    """
    return UnderscoreFunction("reverse", expr)


def levenshtein_distance(a: Underscore | Any, b: Underscore | Any):
    """
    Compute the Levenshtein distance between two strings.

    Parameters
    ----------
    a
        The first string.
    b
        The second string.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    email: str
    ...    name_email_sim: int = F.levenshtein_distance(_.name, _.email)
    """
    return UnderscoreFunction("levenshtein_distance", a, b)


def lower(expr: Underscore | Any):
    """
    Convert a string to lowercase.

    Parameters
    ----------
    expr
        The string to convert to lowercase.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    normalized: str = F.trim(F.lower(_.name))
    """
    return UnderscoreFunction("lower", expr)


def upper(expr: Underscore | Any):
    """
    Convert a string to uppercase.

    Parameters
    ----------
    expr
        The string to convert to uppercase.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    category: str
    ...    normalized: str = F.trim(F.upper(_.category))
    """
    return UnderscoreFunction("upper", expr)


def string_to_bytes(expr: Any, encoding: Literal["utf-8", "hex", "base64"]):
    """
    Convert a string to bytes using the specified encoding.

    Parameters
    ----------
    expr
        An underscore expression for a feature to a
        string feature that should be converted to bytes.
    encoding
        The encoding to use when converting the string to bytes.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    name: str
    ...    hashed_name: bytes = F.string_to_bytes(_.name, encoding="utf-8")
    """
    return UnderscoreStringToBytes(expr, encoding)


def bytes_to_string(expr: Any, encoding: Literal["utf-8", "hex", "base64"]):
    """
    Convert bytes to a string using the specified encoding.

    Parameters
    ----------
    expr
        A bytes feature to convert to a string.
    encoding
        The encoding to use when converting the bytes to a string.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    name: str
    ...    hashed_name: bytes
    ...    decoded_name: str = F.bytes_to_string(_.hashed_name, encoding="utf-8")
    """
    return UnderscoreBytesToString(expr, encoding)


########################################################################################################################
# URLs                                                                                                                 #
########################################################################################################################


def url_extract_protocol(expr: Any):
    """
    Extract the protocol from a URL.

    For example, the protocol of `https://www.google.com/cats` is `https`.

    Parameters
    ----------
    expr
        The URL to extract the protocol from.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Company:
    ...     id: int
    ...     website: str
    ...     protocol: str = F.url_extract_protocol(_.website)
    """
    return UnderscoreFunction("url_extract_protocol", expr)


def url_extract_host(expr: Any):
    """
    Extract the host from a URL.

    For example, the host of `https://www.google.com/cats` is `www.google.com`.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Company:
    ...     id: int
    ...     website: str
    ...     host: str = F.url_extract_host(_.website)
    """
    return UnderscoreFunction("url_extract_host", expr)


def url_extract_path(expr: Any):
    """Extract the path from a URL.

    For example, the host of `https://www.google.com/cats` is `/cats`.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features
    >>> @features
    ... class Company:
    ...     id: int
    ...     website: str
    ...     path: str = F.url_extract_path(_.website)
    """
    return UnderscoreFunction("url_extract_path", expr)


########################################################################################################################
# Misc                                                                                                                 #
########################################################################################################################


def md5(expr: Any):
    """
    Compute the MD5 hash of some bytes.

    Parameters
    ----------
    expr
        A bytes feature to hash.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    bytes_feature: bytes
    ...    md5_bytes: bytes = F.md5(_.bytes_feature)
    """
    return UnderscoreMD5(expr)


def coalesce(*vals: Any):
    """
    Return the first non-null entry

    Parameters
    ----------
    vals
        Expressions to coalesce. They can be a combination of underscores and literals,
        though types must be compatible (ie do not coalesce int and string).

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    a: int | None
    ...    b: int | None
    ...    c: int = F.coalesce(_.a, _.b, 7)
    """
    return UnderscoreCoalesce(*vals)


def sagemaker_predict(
    body: Underscore | Any,
    *,
    endpoint: str,
    content_type: str | None = None,
    target_model: str | None = None,
    target_variant: str | None = None,
    aws_access_key_id_override: str | None = None,
    aws_secret_access_key_override: str | None = None,
    aws_session_token_override: str | None = None,
    aws_region_override: str | None = None,
    aws_profile_name_override: str | None = None,
):
    """
    Runs a sagemaker prediction on the specified endpoint, passing in the serialized bytes as a feature.

    Parameters
    ----------
    body
        Bytes feature to be passed as the serialized input to the sagemaker endpoint.
    endpoint
        The name of the sagemaker endpoint.
    content_type
        The content type of the input data. If not specified, the content type will be inferred from the endpoint.
    target_model
        An optional argument which specifies the target model for the prediction.
        This should only be used for multimodel sagemaker endpoints.
    target_variant
        An optional argument which specifies the target variant for the prediction.
        This should only be used for multi variant sagemaker endpoints.
    aws_access_key_id_override
        An optional argument which specifies the AWS access key ID to use for the prediction.
    aws_secret_access_key_override
        An optional argument which specifies the AWS secret access key to use for the prediction.
    aws_session_token_override
        An optional argument which specifies the AWS session token to use for the prediction.
    aws_region_override
        An optional argument which specifies the AWS region to use for the prediction.
    aws_profile_name_override
        An optional argument which specifies the AWS profile name to use for the prediction

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features
    >>> @features
    ... class User:
    ...    id: str
    ...    encoded_sagemaker_data: bytes
    ...    prediction: float = F.sagemaker_predict(
    ...        _.encoded_sagemaker_data,
    ...        endpoint="prediction-model_1.0.1_2024-09-16",
    ...        target_model="model_v2.tar.gz",
    ...        target_variant="blue"
    ...    )
    """
    return UnderscoreSagemakerPredict(
        body,
        endpoint=endpoint,
        content_type=content_type,
        target_model=target_model,
        target_variant=target_variant,
        aws_access_key_id_override=aws_access_key_id_override,
        aws_secret_access_key_override=aws_secret_access_key_override,
        aws_session_token_override=aws_session_token_override,
        aws_region_override=aws_region_override,
        aws_profile_name_override=aws_profile_name_override,
    )


def json_value(expr: Underscore, path: Union[str, Underscore]):
    """
    Extract a scalar from a JSON feature using a JSONPath expression. The value of the referenced path must be a JSON
    scalar (boolean, number, string).

    Parameters
    ----------
    expr
        The JSON feature to query.
    path
        The JSONPath-like expression to extract the scalar from the JSON feature.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk import JSON
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    raw: JSON
    ...    foo_value: str = F.json_value(_.raw, "$.foo.bar")
    """

    return UnderscoreGetJSONValue(expr, path)


def gunzip(expr: Underscore):
    """
    Decompress a GZIP-compressed bytes feature.

    Parameters
    ----------
    expr
        The GZIP-compressed bytes feature to decompress.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    compressed_data: bytes
    ...    decompressed_data: bytes = F.gunzip(_.compressed_data)
    """
    return UnderscoreGunzip(expr)


def cosine_similarity(a: Underscore, b: Underscore):
    """
    Compute the cosine similarity between two vectors.

    Parameters
    ----------
    a
        The first vector.
    b
        The second vector.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    embedding: Vector[1536]
    >>> @features
    ... class Merchant:
    ...    id: Primary[str]
    ...    embedding: Vector[1536]
    >>> @features
    ... class UserMerchant:
    ...    id: Primary[str]
    ...    user_id: User.id
    ...    user: User
    ...    merchant_id: Merchant.id
    ...    merchant: Merchant
    ...    similarity: float = F.cosine_similarity(_.user.embedding, _.merchant.embedding)
    """
    return UnderscoreCosineSimilarity(a, b)


########################################################################################################################
# Mathematical Functions                                                                                               #
########################################################################################################################


def power(a: Underscore | Any, b: Underscore | Any):
    """
    Raise a to the power of b. Alias for `a ** b`.

    Parameters
    ----------
    a
        The base.
    b
        The exponent.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Merchant:
    ...    id: Primary[str]
    ...    amount_std: float
    ...    amount_var: float = F.power(_.amount_std, 2)
    """
    return UnderscoreFunction("power", a, b)


def sin(expr: Underscore | Any):
    """
    Compute the sine of an angle in radians.

    Parameters
    ----------
    expr
        The angle in radians.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Triangle:
    ...    id: Primary[str]
    ...    angle: float
    ...    sin_angle: float = F.sin(_.angle)
    """
    return UnderscoreFunction("sin", expr)


def cos(expr: Underscore | Any):
    """
    Compute the cosine of an angle in radians.

    Parameters
    ----------
    expr
        The angle in radians.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Triangle:
    ...    id: Primary[str]
    ...    angle: float
    ...    cos_angle: float = F.cos(_.angle)
    """
    return UnderscoreFunction("cos", expr)


def ln(expr: Underscore | Any):
    """
    Compute the natural logarithm of a number.

    Parameters
    ----------
    expr
        The number to compute the natural logarithm of.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Triangle:
    ...    id: Primary[str]
    ...    hypotenuse: float
    ...    log_hypotenuse: float = F.ln(_.hypotenuse)
    """
    return UnderscoreFunction("ln", expr)


def exp(expr: Underscore | Any):
    """
    Returns Euler’s number raised to the power of x.

    Parameters
    ----------
    expr
        The exponent to raise Euler's number to.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Triangle:
    ...    id: Primary[str]
    ...    x: float
    ...    e_to_x: float = F.exp(_.x)
    """
    return UnderscoreFunction("exp", expr)


########################################################################################################################
# Date and Time Functions                                                                                              #
########################################################################################################################


def total_seconds(delta: Underscore) -> Underscore:
    """
    Compute the total number of seconds covered in a duration.

    Parameters
    ----------
    delta
        The duration to convert to seconds.

    Examples
    --------
    >>> from datetime import date
    >>> from chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    signup: date
    ...    last_login: date
    ...    signup_to_last_login_days: float = F.total_seconds(_.las_login - _.signup) / (60 * 60 * 24)
    """
    return UnderscoreTotalSeconds(delta)


def unix_seconds(expr: Underscore | Any):
    """
    Extract the number of seconds since the Unix epoch.
    Returned as a float.

    Parameters
    ----------
    expr
        The datetime to extract the number of seconds since the Unix epoch from.

    Examples
    --------
    >>> from datetime import datetime
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: datetime
    ...    unix_seconds: float = F.unix_seconds(_.date)
    """
    return UnderscoreFunction("to_unixtime", expr)


def unix_milliseconds(expr: Underscore | Any):
    """
    Extract the number of milliseconds since the Unix epoch.
    Returned as a float.

    Parameters
    ----------
    expr
        The datetime to extract the number of milliseconds since the Unix epoch from.

    Examples
    --------
    >>> from datetime import datetime
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: datetime
    ...    unix_milliseconds: float = F.unix_milliseconds(_.date)
    """
    return UnderscoreFunction("to_unixtime", expr) * 1000.0


def day_of_month(expr: Underscore | Any):
    """
    Extract the day of the month from a date.

    The supported types for x are date and datetime.

    Parameters
    ----------
    expr
        The date to extract the day of the month from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction
    ...    id: Primary[str]
    ...    date: date
    ...    day: int = F.day_of_month(_.date)
    """
    return UnderscoreFunction("day_of_month", expr)


def day_of_week(expr: Underscore | Any):
    """
    Returns the ISO day of the week from x. The value ranges from 1 (Monday) to 7 (Sunday).

    Parameters
    ----------
    expr
        The date to extract the day of the week from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction
    ...    id: Primary[str]
    ...    date: date
    ...    day: int = F.day_of_week(_.date)
    """
    return UnderscoreFunction("day_of_week", expr)


def day_of_year(expr: Underscore | Any):
    """
    Extract the day of the year from a date.

    The value ranges from 1 to 366.

    Parameters
    ----------
    expr
        The date to extract the day of the year from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: date
    ...    day: int = F.day_of_year(_.date)
    """
    return UnderscoreFunction("day_of_year", expr)


def month_of_year(expr: Underscore | Any):
    """
    Extract the month of the year from a date.

    The value ranges from 1 to 12.

    Parameters
    ----------
    expr
        The date to extract the month of the year from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: date
    ...    month: int = F.month_of_year(_.date)
    """
    return UnderscoreFunction("month", expr)


def week_of_year(expr: Underscore | Any):
    """
    Extract the week of the year from a date.

    The value ranges from 1 to 53.

    Parameters
    ----------
    expr
        The date to extract the week of the year from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: date
    ...    week: int = F.week_of_year(_.date)
    """
    return UnderscoreFunction("week_of_year", expr)


def hour_of_day(expr: Underscore | Any):
    """
    Extract the hour of the day from a datetime.

    The value ranges from 0 to 23.

    Parameters
    ----------
    expr
        The datetime to extract the hour of the day from.

    Examples
    --------
    >>> from datetime import datetime
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: datetime
    ...    hour: int = F.hour_of_day(_.date)
    """
    return UnderscoreFunction("hour", expr)


########################################################################################################################
# Array Functions                                                                                                      #
########################################################################################################################


def slice(arr: Underscore | list[Any], offset: Underscore | int, length: Underscore | int):
    """
    Returns a subset of the original array

    Parameters
    ----------
    arr
        The array to slice
    offset
        Starting index of the slice (0-indexed). If negative, slice starts from the end of the array
    length
        Length of the slice.

    Examples
    --------
    >>> from datetime import datetime
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Wordle:
    ...    id: Primary[str]
    ...    words: list[str] = ["crane", "kayak", "plots", "fight", "exact", "zebra", "hello", "world"]
    ...    three_most_recent_words: list[str] = F.slice(_.words, -3, 3) # computes ["zebra", "hello", "world"]
    """

    if isinstance(offset, int):
        start = offset if offset < 0 else offset + 1
    else:
        start = UnderscoreFunction(
            "if_else", UnderscoreBinaryOp("<", offset, 0), offset, UnderscoreBinaryOp("+", offset, 1)
        )
    return UnderscoreFunction("slice", arr, start, length)


########################################################################################################################
# Additional Aggregations                                                                                              #
########################################################################################################################


def head(dataframe: Underscore | Any, n: Underscore | int):
    """
    Returns the first n items from a dataframe or has-many

    Parameters
    ----------
    dataframe
        the has-many from which the first n items are taken
    n
        how many items to take

    Examples
    --------
    >>> from datetime import datetime
    >>> import chalk.functions as F
    >>> from chalk import has_many, windowed, DataFrame, Windowed
    >>> from chalk.features import _, features, Primary
    >>> @features
    >>> class Merchant:
    ...     id: str
    ...
    >>> @features
    >>> class ConfirmedFraud:
    ...     id: int
    ...     trn_dt: datetime
    ...     is_fraud: int
    ...     mer_id: Primary[Merchant.id]
    ...
    >>> @features
    >>> class MerchantFraud:
    ...     mer_id: Primary[Merchant.id]
    ...     merchant: Merchant
    ...     confirmed_fraud: DataFrame[ConfirmedFraud] = dataframe(
    ...         lambda: ConfirmedFraud.mer_id == MerchantFraud.mer_id,
    ...     )
    ...     first_five_merchant_window_fraud: Windowed[list[int]] = windowed(
    ...         "1d",
    ...         "30d",
    ...         expression=F.head(_.confirmed_fraud[_.trn_dt > _.chalk_window, _.id, _.is_fraud == 1], 5)
    ...     )
    """
    return slice(UnderscoreFunction("array_agg", dataframe), 0, n)


__all__ = (
    "bytes_to_string",
    "coalesce",
    "cos",
    "cosine_similarity",
    "day_of_month",
    "day_of_week",
    "day_of_year",
    "ends_with",
    "exp",
    "gunzip",
    "head",
    "hour_of_day",
    "json_value",
    "like",
    "ln",
    "md5",
    "month_of_year",
    "power",
    "regexp_like",
    "reverse",
    "sagemaker_predict",
    "sin",
    "starts_with",
    "string_to_bytes",
    "slice",
    "total_seconds",
    "trim",
    "unix_milliseconds",
    "unix_seconds",
    "week_of_year",
)
