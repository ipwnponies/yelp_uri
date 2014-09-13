# -*- coding: utf-8 -*-
import re

from yelp_uri import RFC3986

# Disable line number limit for the domains regex:
# pylint: disable=line-too-long

# Generated from generate_domains.py script.
domains = r"ac|academy|accountants|active|actor|ad|ae|aero|af|ag|agency|ai|airforce|al|am|an|ao|aq|ar|archi|army|arpa|as|asia|associates|at|attorney|au|auction|audio|autos|aw|ax|axa|az|ba|bar|bargains|bayern|bb|bd|be|beer|berlin|best|bf|bg|bh|bi|bid|bike|bio|biz|bj|black|blackfriday|blue|bm|bmw|bn|bnpparibas|bo|boo|boutique|br|brussels|bs|bt|build|builders|business|buzz|bv|bw|by|bz|bzh|ca|cab|camera|camp|cancerresearch|capetown|capital|caravan|cards|care|career|careers|cash|cat|catering|cc|cd|center|ceo|cern|cf|cg|ch|cheap|christmas|church|ci|citic|city|ck|cl|claims|cleaning|click|clinic|clothing|club|cm|cn|co|codes|coffee|college|cologne|com|community|company|computer|condos|construction|consulting|contractors|cooking|cool|coop|country|cr|credit|creditcard|cruises|cu|cuisinella|cv|cw|cx|cy|cymru|cz|dad|dance|dating|day|de|deals|degree|democrat|dental|dentist|desi|diamonds|diet|digital|direct|directory|discount|dj|dk|dm|dnp|do|domains|durban|dz|eat|ec|edu|education|ee|eg|email|engineer|engineering|enterprises|equipment|er|es|esq|estate|et|eu|eus|events|exchange|expert|exposed|fail|farm|feedback|fi|finance|financial|fish|fishing|fitness|fj|fk|flights|florist|fm|fo|foo|foundation|fr|frl|frogans|fund|furniture|futbol|ga|gal|gallery|gb|gbiz|gd|ge|gent|gf|gg|gh|gi|gift|gifts|gives|gl|glass|global|globo|gm|gmail|gmo|gmx|gn|gop|gov|gp|gq|gr|graphics|gratis|green|gripe|gs|gt|gu|guide|guitars|guru|gw|gy|hamburg|haus|healthcare|help|here|hiphop|hiv|hk|hm|hn|holdings|holiday|homes|horse|host|hosting|house|how|hr|ht|hu|id|ie|il|im|immo|immobilien|in|industries|info|ing|ink|institute|insure|int|international|investments|io|iq|ir|is|it|je|jetzt|jm|jo|jobs|joburg|jp|juegos|kaufen|ke|kg|kh|ki|kim|kitchen|kiwi|km|kn|koeln|kp|kr|krd|kred|kw|ky|kz|la|lacaixa|land|lawyer|lb|lc|lease|lgbt|li|life|lighting|limited|limo|link|lk|loans|london|lotto|lr|ls|lt|ltda|lu|luxe|luxury|lv|ly|ma|maison|management|mango|market|marketing|mc|md|me|media|meet|melbourne|meme|menu|mg|mh|miami|mil|mini|mk|ml|mm|mn|mo|mobi|moda|moe|monash|mortgage|moscow|motorcycles|mov|mp|mq|mr|ms|mt|mu|museum|mv|mw|mx|my|mz|na|nagoya|name|navy|nc|ne|net|network|neustar|new|nf|ng|ngo|nhk|ni|ninja|nl|no|np|nr|nra|nrw|nu|nyc|nz|okinawa|om|ong|onl|ooo|org|organic|otsuka|ovh|pa|paris|partners|parts|pe|pf|pg|ph|pharmacy|photo|photography|photos|physio|pics|pictures|pink|pizza|pk|pl|place|plumbing|pm|pn|post|pr|praxi|press|pro|prod|productions|properties|property|ps|pt|pub|pw|py|qa|qpon|quebec|re|realtor|recipes|red|rehab|reise|reisen|ren|rentals|repair|report|republican|rest|restaurant|reviews|rich|rio|ro|rocks|rodeo|rs|rsvp|ru|ruhr|rw|ryukyu|sa|saarland|sarl|sb|sc|sca|scb|schmidt|schule|scot|sd|se|services|sexy|sg|sh|shiksha|shoes|si|singles|sj|sk|sl|sm|sn|so|social|software|sohu|solar|solutions|soy|space|spiegel|sr|st|su|supplies|supply|support|surf|surgery|suzuki|sv|sx|sy|systems|sz|tatar|tattoo|tax|tc|td|technology|tel|tf|tg|th|tienda|tips|tirol|tj|tk|tl|tm|tn|to|today|tokyo|tools|top|town|toys|tp|tr|trade|training|travel|tt|tv|tw|tz|ua|ug|uk|university|uno|uol|us|uy|uz|va|vacations|vc|ve|vegas|ventures|versicherung|vet|vg|vi|viajes|villas|vision|vlaanderen|vn|vodka|vote|voting|voto|voyage|vu|wales|wang|watch|webcam|website|wed|wf|whoswho|wien|wiki|williamhill|wme|works|ws|wtc|wtf|xn--1qqw23a|xn--3bst00m|xn--3ds443g|xn--3e0b707e|xn--45brj9c|xn--4gbrim|xn--55qw42g|xn--55qx5d|xn--6frz82g|xn--6qq986b3xl|xn--80adxhks|xn--80ao21a|xn--80asehdb|xn--80aswg|xn--90a3ac|xn--c1avg|xn--cg4bki|xn--clchc0ea0b2g2a9gcd|xn--czr694b|xn--czru2d|xn--d1acj3b|xn--fiq228c5hs|xn--fiq64b|xn--fiqs8s|xn--fiqz9s|xn--fpcrj9c3d|xn--fzc2c9e2c|xn--gecrj9c|xn--h2brj9c|xn--i1b6b1a6a2e|xn--io0a7i|xn--j1amh|xn--j6w193g|xn--kprw13d|xn--kpry57d|xn--kput3i|xn--l1acc|xn--lgbbat1ad8j|xn--mgb9awbf|xn--mgba3a4f16a|xn--mgbaam7a8h|xn--mgbab2bd|xn--mgbayh7gpa|xn--mgbbh1a71e|xn--mgbc0a9azcg|xn--mgberp4a5d4ar|xn--mgbx4cd0ab|xn--ngbc5azd|xn--nqv7f|xn--nqv7fs00ema|xn--o3cw4h|xn--ogbpf8fl|xn--p1ai|xn--pgbs0dh|xn--q9jyb4c|xn--rhqv96g|xn--s9brj9c|xn--ses554g|xn--unup4y|xn--vhquv|xn--wgbh1c|xn--wgbl6a|xn--xhq521b|xn--xkc2al3hye2a|xn--xkc2dl3a5ee0h|xn--yfro4i67o|xn--ygbi2ammx|xn--zfr164b|xxx|xyz|yachts|yandex|ye|yokohama|youtube|yt|za|zm|zone|zw"  # NOQA

# A regex for finding urls in free-form text.
# This regex is space-indented, so that it looks OK on ReviewBoard
#
# the following regex works like this:
# first part of URL is either:
#   http:// or https:// followed by any dotted hostname
#    or
#   dotted hostname where last part is com, net, org, etc. (so we don't accidentally linkify wrong stuff)
#    and in this case, the hostname cannot be preceded by dot or @ (or alphanum), as this causes weird matches
#
# (optional) second part of URL can consist of lots of differrent characters,
#  but cannot end in .!,?;:( because those are maybe not meant to be part of the URL.
# NOTE: regex has been recently modified to allow a url to end in ")" so it can support urls
# that contain parenthesis, such as wikipedia urls (e.g. 'http://en.wikipedia.org/wiki/Ham_(disambiguation)')
# linkify_url has also been changed to look for urls ending in a ")" that do not have a matching "(", and moves
# it outside of the closing link tag if found.
url_regex = re.compile(
    r"""
        # Don't start in the middle of something.
        (?<!  [\w.@/:-] )
        (?!  mailto: )
        # Looking for a domain name
        (
            # we look for a known prefix
            (
                https?://
            |
                www\.
            )
            ([^%(not_userinfo)s]+@)? # maybe a user?
            [^%(not_regname)s]+
            \.
            [^%(not_regname)s.]{2,}
            (:\d+)? # maybe a port?
        |
            # or else look for a domain name with a known suffix.
            # We're more strict about dots / userinfo in this case, since the
            # user intent is more ambiguous.
            (   # one or more domain segments
                [^%(not_regname)s.]+\.
            )+
            (%(domains)s)
            (:\d+)? # maybe a port?
        )
        # An optional path/query/fragment component
        (
            [/?#]
            (
                # Figure out if we have parens in our url
                (?=(?P<HAS_PARENS>
                    [^:%(not_url)s]*\(
                ))?
                (?(HAS_PARENS)
                    # If we have parens, we use this:
                    [^%(not_url)s]*
                    [^%(bad_end)s]
                |
                    # Otherwise, we use this:
                    [^\)%(not_url)s]*
                    [^\)%(bad_end)s]
                )
            )?
        )?
        # Look-ahead to make sure the URL ends nicely.
        (?=
            [\)%(bad_end)s]
        |
            $
        )
    """ % dict(
        vars(RFC3986.re),
        domains=domains,
    ),
    re.VERBOSE | re.UNICODE | re.IGNORECASE,
)


# A regex for finding email addresses in free-form text.
email_regex = re.compile(
    r"""
        (?: # Don't start in the middle of something.
            (?<!  [\w.@/:-] )
            |
            (?<= mailto:// )
        )
        (   # A local-part in an email address
            # Can't have percent signs. See: http://www.postfix.org/postconf.5.html#allow_percent_hack
            [^%(not_userinfo)s%%]+
        )
        @ # At sign
        ( # Start of FQDN
            (?: # one or more domain segments
                [^%(not_regname)s.]+\.
            )+
            [^%(not_regname)s.]{2,} # Top-level domain
        ) # End of FQDN
    """ % vars(RFC3986.re),
    re.VERBOSE | re.UNICODE
)

# List the names that this module "really" exports.
__all__ = (
    'url_regex',
    'email_regex',
)
# vim:et:sts=4
