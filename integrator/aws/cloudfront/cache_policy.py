from pulumi_aws import cloudfront


class CachePolicy(cloudfront.CachePolicy):
    def __init__(
        self,
        resource_name: str,
        default_ttl: int = 300,
        max_ttl: int = 300,
        min_ttl: int = 60,
        **kwargs,
    ) -> None:
        """Create a new Cache Policy.

        Args:
            resource_name (str): The name of the Cache Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/cachepolicy/#inputs)
        """
        kwargs.setdefault(
            "parameters_in_cache_key_and_forwarded_to_origin",
            cloudfront.CachePolicyParametersInCacheKeyAndForwardedToOriginArgs(
                enable_accept_encoding_gzip=True,
                enable_accept_encoding_brotli=True,
                cookies_config=cloudfront.CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigArgs(
                    cookie_behavior="all",
                ),
                headers_config=cloudfront.CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigArgs(
                    header_behavior="none",
                ),
                query_strings_config=cloudfront.CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigArgs(
                    query_string_behavior="none",
                ),
            ),
        )
        super().__init__(
            resource_name,
            default_ttl=default_ttl,
            max_ttl=max_ttl,
            min_ttl=min_ttl,
            **kwargs,
        )
