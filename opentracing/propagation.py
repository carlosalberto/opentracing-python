# Copyright (c) 2016 The OpenTracing Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import absolute_import


class UnsupportedFormatException(Exception):
    """UnsupportedFormatException should be used when the provided format
    value is unknown or disallowed by the :class:`Tracer`.

    See :meth:`Tracer.inject()` and :meth:`Tracer.extract()`.
    """
    pass


class InvalidCarrierException(Exception):
    """InvalidCarrierException should be used when the provided carrier
    instance does not match what the `format` argument requires.

    See :meth:`Tracer.inject()` and :meth:`Tracer.extract()`.
    """
    pass


class SpanContextCorruptedException(Exception):
    """SpanContextCorruptedException should be used when the underlying
    :class:`SpanContext` state is seemingly present but not well-formed.

    See :meth:`Tracer.inject()` and :meth:`Tracer.extract()`.
    """
    pass


class Format(object):
    """A namespace for builtin carrier formats.

    These static constants are intended for use in the :meth:`Tracer.inject()`
    and :meth:`Tracer.extract()` methods. E.g.::

        tracer.inject(span.context, Format.BINARY, binary_carrier)

    """

    BINARY = 'binary'
    """
    The BINARY format represents SpanContexts in an opaque bytearray carrier.

    For both :meth:`Tracer.inject()` and :meth:`Tracer.extract()` the carrier
    should be a bytearray instance. :meth:`Tracer.inject()` must append to the
    bytearray carrier (rather than replace its contents).
    """

    TEXT_MAP = 'text_map'
    """
    The TEXT_MAP format represents :class:`SpanContext`\ s in a python ``dict``
    mapping from strings to strings.

    Both the keys and the values have unrestricted character sets (unlike the
    HTTP_HEADERS format).

    NOTE: The TEXT_MAP carrier ``dict`` may contain unrelated data (e.g.,
    arbitrary gRPC metadata). As such, the :class:`Tracer` implementation
    should use a prefix or other convention to distinguish tracer-specific
    key:value pairs.
    """

    HTTP_HEADERS = 'http_headers'
    """
    The HTTP_HEADERS format represents :class:`SpanContext`\ s in a python
    ``dict`` mapping from character-restricted strings to strings.

    Keys and values in the HTTP_HEADERS carrier must be suitable for use as
    HTTP headers (without modification or further escaping). That is, the
    keys have a greatly restricted character set, casing for the keys may not
    be preserved by various intermediaries, and the values should be
    URL-escaped.

    NOTE: The HTTP_HEADERS carrier ``dict`` may contain unrelated data (e.g.,
    arbitrary gRPC metadata). As such, the :class:`Tracer` implementation
    should use a prefix or other convention to distinguish tracer-specific
    key:value pairs.
    """
