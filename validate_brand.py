#!/usr/bin/env python3
"""
FinTechCo Brand Validation Script
Validates content against FinTechCo brand guidelines including colors, fonts, tone, and messaging.
"""

import json
import re
from dataclasses import asdict, dataclass


@dataclass
class BrandGuidelines:
    """Brand guidelines configuration"""

    brand_name: str
    primary_colors: list[str]
    secondary_colors: list[str]
    fonts: list[str]
    tone_keywords: list[str]
    prohibited_words: list[str]
    tagline: str | None = None
    logo_usage_rules: dict | None = None


@dataclass
class ValidationResult:
    """Result of brand validation"""

    passed: bool
    score: float
    violations: list[str]
    warnings: list[str]
    suggestions: list[str]


class BrandValidator:
    """Validates content against FinTechCo brand guidelines"""

    def __init__(self, guidelines: BrandGuidelines):
        self.guidelines = guidelines

    def validate_colors(self, content: str) -> tuple[list[str], list[str]]:
        """
        Validate color usage in content (hex codes and RGB values).
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        hex_pattern = r"#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}"
        found_colors = re.findall(hex_pattern, content)

        rgb_pattern = r"rgb\s*\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}\s*\)"
        found_colors.extend(re.findall(rgb_pattern, content, re.IGNORECASE))

        approved_colors = self.guidelines.primary_colors + self.guidelines.secondary_colors

        for color in found_colors:
            if color.upper() not in [c.upper() for c in approved_colors]:
                violations.append(f"Unapproved color used: {color}")

        return violations, warnings

    def validate_fonts(self, content: str) -> tuple[list[str], list[str]]:
        """
        Validate font usage in content (CSS font-family declarations).
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        font_patterns = [
            r'font-family\s*:\s*["\']?([^;"\']+)["\']?',
            r"font:\s*[^;]*\s+([A-Za-z][A-Za-z\s]+)(?:,|;|\s+\d)",
        ]

        found_fonts = []
        for pattern in font_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            found_fonts.extend(matches)

        for font in found_fonts:
            font_clean = font.strip().lower()
            if not any(approved.lower() in font_clean for approved in self.guidelines.fonts):
                violations.append(f"Unapproved font used: {font.strip()}")

        return violations, warnings

    def validate_tone(self, content: str) -> tuple[list[str], list[str]]:
        """
        Validate tone and messaging against FinTechCo standards.
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        content_lower = content.lower()

        for word in self.guidelines.prohibited_words:
            if word.lower() in content_lower:
                violations.append(f"Prohibited word/phrase used: '{word}'")

        tone_matches = sum(
            1 for keyword in self.guidelines.tone_keywords if keyword.lower() in content_lower
        )

        if tone_matches == 0 and len(content.strip()) > 100:
            warnings.append(
                "Content may not align with FinTechCo brand tone. "
                f"Consider using terms like: {', '.join(self.guidelines.tone_keywords[:5])}"
            )

        # Flag vague/uncertain language
        vague_patterns = [r"\bwe think\b", r"\bmaybe\b", r"\bsort of\b", r"\bapproximately\b"]
        for pattern in vague_patterns:
            if re.search(pattern, content_lower):
                warnings.append(
                    f"Vague language detected ('{pattern.strip(r'\\b')}') — FinTechCo tone requires precision"
                )

        return violations, warnings

    def validate_brand_name(self, content: str) -> tuple[list[str], list[str]]:
        """
        Validate brand name capitalization and usage.
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        brand_pattern = re.compile(re.escape(self.guidelines.brand_name), re.IGNORECASE)
        matches = brand_pattern.findall(content)

        for match in matches:
            if match != self.guidelines.brand_name:
                violations.append(
                    f"Incorrect brand name capitalization: '{match}' should be '{self.guidelines.brand_name}'"
                )

        return violations, warnings

    def validate_number_format(self, content: str) -> tuple[list[str], list[str]]:
        """
        Validate number formatting against FinTechCo standards.
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        # Flag minus-sign negatives (should use parentheses for currency)
        minus_currency = re.findall(r"-\$[\d,]+\.?\d*", content)
        for match in minus_currency:
            warnings.append(
                f"Negative currency '{match}' should use parentheses format: "
                f"({match.replace('-', '')})"
            )

        # Flag dates in wrong format (MM/DD/YYYY or DD-MM-YYYY)
        wrong_date = re.findall(r"\b\d{1,2}[/\-]\d{1,2}[/\-]\d{4}\b", content)
        for match in wrong_date:
            warnings.append(
                f"Date '{match}' should use 'Month DD, YYYY' format (e.g., October 29, 2026)"
            )

        return violations, warnings

    def calculate_score(self, violations: list[str], warnings: list[str]) -> float:
        """Calculate brand compliance score (0–100)."""
        violation_penalty = len(violations) * 10
        warning_penalty = len(warnings) * 3

        return max(0.0, round(100.0 - violation_penalty - warning_penalty, 2))

    def generate_suggestions(self, violations: list[str], warnings: list[str]) -> list[str]:
        """Generate actionable suggestions based on violations and warnings."""
        suggestions = []

        if any("color" in v.lower() for v in violations):
            suggestions.append(
                "Replace non-brand colors. Primary: #006044 (FinTechCo Green), "
                "#00A651 (Bright Green), #1A1A1A (Ink Black)"
            )

        if any("font" in v.lower() for v in violations):
            suggestions.append(
                "Use the approved font stack: "
                'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
            )

        if any("tone" in w.lower() for w in warnings):
            suggestions.append(
                f"Align with FinTechCo tone. Use keywords: {', '.join(self.guidelines.tone_keywords[:5])}"
            )

        if any("brand name" in v.lower() for v in violations):
            suggestions.append(f"Always write brand name as: {self.guidelines.brand_name}")

        if any("negative currency" in w.lower() for w in warnings):
            suggestions.append(
                "Use parentheses for negative currency values: ($1,234.56) not -$1,234.56"
            )

        if any("date" in w.lower() for w in warnings):
            suggestions.append("Use date format: Month DD, YYYY (e.g., October 29, 2026)")

        return suggestions

    def validate(self, content: str) -> ValidationResult:
        """
        Run all FinTechCo brand validation checks on content.

        Args:
            content: Text or markup content to validate

        Returns:
            ValidationResult with score, violations, warnings, and suggestions
        """
        all_violations = []
        all_warnings = []

        color_v, color_w = self.validate_colors(content)
        all_violations.extend(color_v)
        all_warnings.extend(color_w)

        font_v, font_w = self.validate_fonts(content)
        all_violations.extend(font_v)
        all_warnings.extend(font_w)

        tone_v, tone_w = self.validate_tone(content)
        all_violations.extend(tone_v)
        all_warnings.extend(tone_w)

        brand_v, brand_w = self.validate_brand_name(content)
        all_violations.extend(brand_v)
        all_warnings.extend(brand_w)

        number_v, number_w = self.validate_number_format(content)
        all_violations.extend(number_v)
        all_warnings.extend(number_w)

        score = self.calculate_score(all_violations, all_warnings)
        suggestions = self.generate_suggestions(all_violations, all_warnings)

        return ValidationResult(
            passed=len(all_violations) == 0,
            score=score,
            violations=all_violations,
            warnings=all_warnings,
            suggestions=suggestions,
        )


def load_guidelines_from_json(filepath: str) -> BrandGuidelines:
    """
    Load brand guidelines from a JSON file.

    Args:
        filepath: Path to JSON file containing brand guidelines

    Returns:
        BrandGuidelines object

    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
        TypeError: If required fields are missing
    """
    try:
        with open(filepath) as f:
            data = json.load(f)
        return BrandGuidelines(**data)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Brand guidelines file not found: {filepath}") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON in brand guidelines file: {e.msg}", e.doc, e.pos
        ) from e
    except TypeError as e:
        raise TypeError(f"Missing required fields in brand guidelines: {e}") from e


def get_fintechco_guidelines() -> BrandGuidelines:
    """
    Get FinTechCo brand guidelines.

    Matches the standards defined in SKILL.md.
    Customize this function or use load_guidelines_from_json() for your own organization.

    Returns:
        BrandGuidelines object with FinTechCo standards
    """
    return BrandGuidelines(
        brand_name="FinTechCo",
        primary_colors=["#006044", "#00A651", "#1A1A1A", "#FFFFFF"],
        secondary_colors=["#2E7D32", "#F59E0B", "#DC2626", "#6B7280", "#F0F7F4", "#F9FAFB"],
        fonts=["Inter", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "sans-serif"],
        tone_keywords=[
            "financial",
            "trusted",
            "simplified",
            "future",
            "secure",
            "growth",
            "professional",
            "transparent",
            "reliable",
        ],
        prohibited_words=[
            "cheap",
            "risky",
            "guaranteed returns",
            "get rich",
            "unprofessional",
            "sloppy",
            "inferior",
        ],
        tagline="Your Financial Future, Simplified",
    )


def main():
    """Demonstrate FinTechCo brand validation with example content."""
    guidelines = get_fintechco_guidelines()

    test_content = """
    Welcome to fintechco!

    We think we offer cheap investment solutions with guaranteed returns.

    Our trusted and transparent approach to financial growth is relied upon by thousands.

    Contact us at: font-family: 'Comic Sans MS'
    Primary color: #FF0000
    Background: rgb(255, 0, 0)

    Q3 loss: -$12,345.00
    Report date: 10/29/2026
    """

    validator = BrandValidator(guidelines)
    result = validator.validate(test_content)

    print("=" * 60)
    print("FINTECHCO BRAND VALIDATION REPORT")
    print("=" * 60)
    print(f"\nOverall Status: {'✓ PASSED' if result.passed else '✗ FAILED'}")
    print(f"Compliance Score: {result.score}/100")

    if result.violations:
        print(f"\n❌ VIOLATIONS ({len(result.violations)}):")
        for i, violation in enumerate(result.violations, 1):
            print(f"  {i}. {violation}")

    if result.warnings:
        print(f"\n⚠️  WARNINGS ({len(result.warnings)}):")
        for i, warning in enumerate(result.warnings, 1):
            print(f"  {i}. {warning}")

    if result.suggestions:
        print("\n💡 SUGGESTIONS:")
        for i, suggestion in enumerate(result.suggestions, 1):
            print(f"  {i}. {suggestion}")

    print("\n" + "=" * 60)

    return asdict(result)


if __name__ == "__main__":
    main()
