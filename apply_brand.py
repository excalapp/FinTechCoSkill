"""
Brand application module for FinTechCo document styling.
Applies consistent FinTechCo branding to Excel, PowerPoint, and PDF documents.
Inspired by modern financial services design (Fidelity-style green palette, Inter typography).
"""

from typing import Any


class BrandFormatter:
    """Apply FinTechCo brand guidelines to documents."""

    COLORS = {
        "primary": {
            "fintechco_green": {"hex": "#006044", "rgb": (0, 96, 68)},
            "fintechco_bright_green": {"hex": "#00A651", "rgb": (0, 166, 81)},
            "ink_black": {"hex": "#1A1A1A", "rgb": (26, 26, 26)},
            "white": {"hex": "#FFFFFF", "rgb": (255, 255, 255)},
        },
        "secondary": {
            "success_green": {"hex": "#2E7D32", "rgb": (46, 125, 50)},
            "warning_amber": {"hex": "#F59E0B", "rgb": (245, 158, 11)},
            "error_red": {"hex": "#DC2626", "rgb": (220, 38, 38)},
            "neutral_gray": {"hex": "#6B7280", "rgb": (107, 114, 128)},
            "light_green_tint": {"hex": "#F0F7F4", "rgb": (240, 247, 244)},
            "surface_gray": {"hex": "#F9FAFB", "rgb": (249, 250, 251)},
        },
    }

    FONTS = {
        "primary": "Inter",
        "fallback": ["-apple-system", "BlinkMacSystemFont", "Segoe UI", "sans-serif"],
        "stack": 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
        "sizes": {"h1": 32, "h2": 24, "h3": 18, "body": 11, "caption": 9, "label": 10},
        "weights": {"regular": 400, "medium": 500, "semibold": 600, "bold": 700},
        "line_heights": {"display": 1.15, "heading": 1.25, "body": 1.6, "caption": 1.4},
    }

    COMPANY = {
        "name": "FinTechCo",
        "tagline": "Your Financial Future, Simplified",
        "copyright": "© 2026 FinTechCo. All rights reserved.",
        "website": "www.fintechco.example",
        "logo_path": "assets/fintechco_logo.png",
        "brand_email": "brand@fintechco.example",
    }

    def __init__(self):
        self.colors = self.COLORS
        self.fonts = self.FONTS
        self.company = self.COMPANY

    def format_excel(self, workbook_config: dict[str, Any]) -> dict[str, Any]:
        """
        Apply FinTechCo brand formatting to Excel workbook configuration.

        Args:
            workbook_config: Excel workbook configuration dictionary

        Returns:
            Branded workbook configuration
        """
        branded_config = workbook_config.copy()

        branded_config["header_style"] = {
            "font": {
                "name": self.fonts["primary"],
                "size": self.fonts["sizes"]["body"],
                "bold": True,
                "color": self.colors["primary"]["white"]["hex"],
            },
            "fill": {
                "type": "solid",
                "color": self.colors["primary"]["fintechco_green"]["hex"],
            },
            "alignment": {"horizontal": "center", "vertical": "center"},
            "border": {
                "style": "thin",
                "color": self.colors["secondary"]["neutral_gray"]["hex"],
            },
        }

        branded_config["subheader_style"] = {
            "font": {
                "name": self.fonts["primary"],
                "size": self.fonts["sizes"]["body"],
                "bold": True,
                "color": self.colors["primary"]["ink_black"]["hex"],
            },
            "fill": {
                "type": "solid",
                "color": self.colors["secondary"]["light_green_tint"]["hex"],
            },
        }

        branded_config["cell_style"] = {
            "font": {
                "name": self.fonts["primary"],
                "size": self.fonts["sizes"]["body"],
                "color": self.colors["primary"]["ink_black"]["hex"],
            },
            "alignment": {"horizontal": "left", "vertical": "center"},
            "border": {
                "style": "thin",
                "color": self.colors["secondary"]["neutral_gray"]["hex"],
            },
        }

        branded_config["number_style"] = {
            "alignment": {"horizontal": "right"},
            "positive_color": self.colors["secondary"]["success_green"]["hex"],
            "negative_color": self.colors["secondary"]["error_red"]["hex"],
            "negative_format": "($#,##0.00)",
        }

        branded_config["alternating_rows"] = {
            "enabled": True,
            "color": self.colors["secondary"]["light_green_tint"]["hex"],
        }

        branded_config["chart_colors"] = self.get_chart_palette(6)

        branded_config["gridlines"] = {
            "color": "#E5E7EB",
            "width": 0.5,
        }

        return branded_config

    def format_powerpoint(self, presentation_config: dict[str, Any]) -> dict[str, Any]:
        """
        Apply FinTechCo brand formatting to PowerPoint presentation configuration.

        Args:
            presentation_config: PowerPoint configuration dictionary

        Returns:
            Branded presentation configuration
        """
        branded_config = presentation_config.copy()

        branded_config["master"] = {
            "background_color": self.colors["primary"]["white"]["hex"],
            "top_bar": {
                "height": 0.08,
                "color": self.colors["primary"]["fintechco_green"]["hex"],
            },
            "title_area": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["h1"],
                "weight": self.fonts["weights"]["bold"],
                "color": self.colors["primary"]["ink_black"]["hex"],
                "position": {"x": 0.5, "y": 0.15, "width": 9, "height": 1.2},
            },
            "content_area": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["body"],
                "weight": self.fonts["weights"]["regular"],
                "color": self.colors["primary"]["ink_black"]["hex"],
                "line_height": self.fonts["line_heights"]["body"],
                "position": {"x": 0.5, "y": 1.7, "width": 9, "height": 5.3},
            },
            "footer": {
                "show_slide_number": True,
                "show_date": True,
                "company_name": self.company["name"],
                "text_color": self.colors["secondary"]["neutral_gray"]["hex"],
                "font_size": self.fonts["sizes"]["caption"],
            },
        }

        branded_config["title_slide"] = {
            "background": self.colors["primary"]["fintechco_green"]["hex"],
            "title_color": self.colors["primary"]["white"]["hex"],
            "subtitle_color": self.colors["primary"]["white"]["hex"],
            "tagline": self.company["tagline"],
            "tagline_color": self.colors["primary"]["fintechco_bright_green"]["hex"],
            "include_logo": True,
            "logo_position": {"x": 0.5, "y": 0.4, "width": 1.8},
        }

        branded_config["section_divider_slide"] = {
            "left_band": {
                "width_pct": 0.2,
                "color": self.colors["primary"]["fintechco_green"]["hex"],
            },
            "background": self.colors["primary"]["white"]["hex"],
            "title_color": self.colors["primary"]["ink_black"]["hex"],
            "title_font_size": self.fonts["sizes"]["h1"],
        }

        branded_config["content_slide"] = {
            "top_bar": {
                "height": 0.08,
                "color": self.colors["primary"]["fintechco_green"]["hex"],
            },
            "title_style": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["h2"],
                "weight": self.fonts["weights"]["bold"],
                "color": self.colors["primary"]["ink_black"]["hex"],
            },
            "bullet_style": {
                "level1": "•",
                "level2": "–",
                "level3": "▪",
                "indent": 0.25,
                "line_height": 1.4,
                "max_bullets": 5,
            },
        }

        branded_config["closing_slide"] = {
            "background": self.colors["primary"]["fintechco_green"]["hex"],
            "title_color": self.colors["primary"]["white"]["hex"],
            "website_color": self.colors["primary"]["fintechco_bright_green"]["hex"],
            "website": self.company["website"],
        }

        branded_config["charts"] = {
            "color_scheme": self.get_chart_palette(6),
            "gridlines": {
                "color": "#E5E7EB",
                "width": 0.5,
            },
            "font": {
                "name": self.fonts["primary"],
                "size": self.fonts["sizes"]["caption"],
                "color": self.colors["primary"]["ink_black"]["hex"],
            },
            "no_3d": True,
            "no_gradients": True,
        }

        return branded_config

    def format_pdf(self, document_config: dict[str, Any]) -> dict[str, Any]:
        """
        Apply FinTechCo brand formatting to PDF document configuration.

        Args:
            document_config: PDF document configuration dictionary

        Returns:
            Branded document configuration
        """
        branded_config = document_config.copy()

        branded_config["page"] = {
            "margins": {"top": 1, "bottom": 1, "left": 1, "right": 1},
            "size": "letter",
            "orientation": "portrait",
        }

        branded_config["header"] = {
            "height": 0.75,
            "border_bottom": {
                "color": self.colors["primary"]["fintechco_green"]["hex"],
                "width": 2,
            },
            "content": {
                "left": {"type": "logo", "width": 1.5},
                "center": {
                    "type": "text",
                    "content": document_config.get("title", "Document"),
                    "font": self.fonts["primary"],
                    "size": self.fonts["sizes"]["body"],
                    "weight": self.fonts["weights"]["semibold"],
                    "color": self.colors["primary"]["ink_black"]["hex"],
                },
                "right": {"type": "page_number", "format": "Page {page} of {total}"},
            },
        }

        branded_config["footer"] = {
            "height": 0.5,
            "border_top": {
                "color": self.colors["secondary"]["neutral_gray"]["hex"],
                "width": 0.5,
            },
            "content": {
                "left": {
                    "type": "text",
                    "content": self.company["copyright"],
                    "font": self.fonts["primary"],
                    "size": self.fonts["sizes"]["caption"],
                    "color": self.colors["secondary"]["neutral_gray"]["hex"],
                },
                "center": {"type": "date", "format": "%B %d, %Y"},
                "right": {"type": "text", "content": "Confidential"},
            },
        }

        branded_config["styles"] = {
            "heading1": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["h1"],
                "weight": self.fonts["weights"]["bold"],
                "color": self.colors["primary"]["fintechco_green"]["hex"],
                "spacing_after": 14,
                "line_height": self.fonts["line_heights"]["heading"],
            },
            "heading2": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["h2"],
                "weight": self.fonts["weights"]["semibold"],
                "color": self.colors["primary"]["ink_black"]["hex"],
                "spacing_after": 12,
                "line_height": self.fonts["line_heights"]["heading"],
            },
            "heading3": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["h3"],
                "weight": self.fonts["weights"]["semibold"],
                "color": self.colors["primary"]["ink_black"]["hex"],
                "spacing_after": 10,
                "line_height": self.fonts["line_heights"]["heading"],
            },
            "body": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["body"],
                "weight": self.fonts["weights"]["regular"],
                "color": self.colors["primary"]["ink_black"]["hex"],
                "line_spacing": self.fonts["line_heights"]["body"],
                "paragraph_spacing": 14,
            },
            "caption": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["caption"],
                "weight": self.fonts["weights"]["regular"],
                "color": self.colors["secondary"]["neutral_gray"]["hex"],
                "italic": True,
                "line_height": self.fonts["line_heights"]["caption"],
            },
            "label": {
                "font": self.fonts["primary"],
                "size": self.fonts["sizes"]["label"],
                "weight": self.fonts["weights"]["medium"],
                "color": self.colors["secondary"]["neutral_gray"]["hex"],
                "uppercase": True,
                "letter_spacing": "0.05em",
            },
        }

        branded_config["table_style"] = {
            "header": {
                "background": self.colors["primary"]["fintechco_green"]["hex"],
                "text_color": self.colors["primary"]["white"]["hex"],
                "bold": True,
                "font_size": self.fonts["sizes"]["body"],
            },
            "subheader": {
                "background": self.colors["secondary"]["light_green_tint"]["hex"],
                "text_color": self.colors["primary"]["ink_black"]["hex"],
                "bold": True,
            },
            "rows": {
                "alternating_color": self.colors["secondary"]["light_green_tint"]["hex"],
                "border_color": self.colors["secondary"]["neutral_gray"]["hex"],
                "border_width": 0.5,
            },
            "number_alignment": "right",
            "text_alignment": "left",
            "positive_color": self.colors["secondary"]["success_green"]["hex"],
            "negative_color": self.colors["secondary"]["error_red"]["hex"],
        }

        return branded_config

    def validate_colors(self, colors_used: list[str]) -> dict[str, Any]:
        """
        Validate that colors match FinTechCo brand guidelines.

        Args:
            colors_used: List of hex color codes used in document

        Returns:
            Validation results with corrections if needed
        """
        results = {"valid": True, "corrections": [], "warnings": []}

        approved_colors = []
        for category in self.colors.values():
            for color in category.values():
                approved_colors.append(color["hex"].upper())

        for color in colors_used:
            color_upper = color.upper()
            if color_upper not in approved_colors:
                results["valid"] = False
                closest = self._find_closest_brand_color(color)
                results["corrections"].append(
                    {
                        "original": color,
                        "suggested": closest,
                        "message": f"Non-brand color {color} should be replaced with {closest}",
                    }
                )

        return results

    def _find_closest_brand_color(self, color: str) -> str:
        """Find the closest FinTechCo brand color to a given hex color via Euclidean distance."""
        try:
            r = int(color.lstrip("#")[0:2], 16)
            g = int(color.lstrip("#")[2:4], 16)
            b = int(color.lstrip("#")[4:6], 16)
        except (ValueError, IndexError):
            return self.colors["primary"]["fintechco_green"]["hex"]

        best_hex = self.colors["primary"]["fintechco_green"]["hex"]
        best_dist = float("inf")

        for category in self.colors.values():
            for brand_color in category.values():
                br, bg, bb = brand_color["rgb"]
                dist = (r - br) ** 2 + (g - bg) ** 2 + (b - bb) ** 2
                if dist < best_dist:
                    best_dist = dist
                    best_hex = brand_color["hex"]

        return best_hex

    def apply_watermark(self, document_type: str) -> dict[str, Any]:
        """
        Generate watermark configuration for FinTechCo documents.

        Args:
            document_type: Type of document ('draft', 'confidential', 'sample')

        Returns:
            Watermark configuration
        """
        watermarks = {
            "draft": {
                "text": "DRAFT",
                "color": self.colors["secondary"]["neutral_gray"]["hex"],
                "opacity": 0.08,
                "angle": 45,
                "font": self.fonts["primary"],
                "font_size": 72,
            },
            "confidential": {
                "text": "CONFIDENTIAL",
                "color": self.colors["secondary"]["error_red"]["hex"],
                "opacity": 0.08,
                "angle": 45,
                "font": self.fonts["primary"],
                "font_size": 60,
            },
            "sample": {
                "text": "SAMPLE",
                "color": self.colors["secondary"]["warning_amber"]["hex"],
                "opacity": 0.1,
                "angle": 45,
                "font": self.fonts["primary"],
                "font_size": 72,
            },
        }

        return watermarks.get(document_type, watermarks["draft"])

    def get_chart_palette(self, num_series: int = 4) -> list[str]:
        """
        Get the FinTechCo brand color palette for charts.

        Args:
            num_series: Number of data series (up to 6)

        Returns:
            List of hex color codes
        """
        palette = [
            self.colors["primary"]["fintechco_green"]["hex"],       # #006044
            self.colors["primary"]["fintechco_bright_green"]["hex"],# #00A651
            self.colors["secondary"]["neutral_gray"]["hex"],        # #6B7280
            self.colors["secondary"]["warning_amber"]["hex"],       # #F59E0B
            self.colors["secondary"]["success_green"]["hex"],       # #2E7D32
            self.colors["secondary"]["error_red"]["hex"],           # #DC2626
        ]

        return palette[:num_series]

    def format_number(self, value: float, format_type: str = "general") -> str:
        """
        Format numbers according to FinTechCo brand standards.

        Args:
            value: Numeric value to format
            format_type: One of 'currency', 'percentage', 'large_number', 'general'

        Returns:
            Formatted string
        """
        if format_type == "currency":
            if value < 0:
                return f"(${abs(value):,.2f})"
            return f"${value:,.2f}"
        elif format_type == "percentage":
            return f"{value:.2f}%"
        elif format_type == "large_number":
            if abs(value) >= 1_000_000_000:
                return f"${value / 1_000_000_000:.1f}B"
            elif abs(value) >= 1_000_000:
                return f"${value / 1_000_000:.1f}M"
            elif abs(value) >= 1_000:
                return f"${value / 1_000:.1f}K"
            return f"${value:.0f}"
        else:
            return f"{value:,.0f}" if abs(value) >= 1000 else f"{value:.2f}"


def apply_brand_to_document(document_type: str, config: dict[str, Any]) -> dict[str, Any]:
    """
    Apply FinTechCo branding to any document type.

    Args:
        document_type: One of 'excel', 'powerpoint' / 'pptx', 'pdf'
        config: Document configuration dictionary

    Returns:
        Branded configuration dictionary
    """
    formatter = BrandFormatter()

    if document_type.lower() == "excel":
        return formatter.format_excel(config)
    elif document_type.lower() in ["powerpoint", "pptx"]:
        return formatter.format_powerpoint(config)
    elif document_type.lower() == "pdf":
        return formatter.format_pdf(config)
    else:
        raise ValueError(f"Unsupported document type: {document_type}. Use 'excel', 'powerpoint', or 'pdf'.")


if __name__ == "__main__":
    excel_config = {"title": "Q3 Portfolio Report", "sheets": ["Summary", "Holdings", "Performance"]}
    branded_excel = apply_brand_to_document("excel", excel_config)
    print("FinTechCo Branded Excel Configuration:")
    print(branded_excel)

    ppt_config = {"title": "Annual Investment Review", "num_slides": 12}
    branded_ppt = apply_brand_to_document("powerpoint", ppt_config)
    print("\nFinTechCo Branded PowerPoint Configuration:")
    print(branded_ppt)

    pdf_config = {"title": "Investment Proposal — October 2026"}
    branded_pdf = apply_brand_to_document("pdf", pdf_config)
    print("\nFinTechCo Branded PDF Configuration:")
    print(branded_pdf)
